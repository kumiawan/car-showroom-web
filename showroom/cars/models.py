from django.db import models
from decimal import Decimal
from django.db.models import Sum
from django.utils import timezone

class Car(models.Model):
    merk = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    tahun = models.IntegerField()
    harga_pasar = models.DecimalField(max_digits=12, decimal_places=2)
    dana_bank = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    suku_bunga = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.merk} {self.model} ({self.tahun})"

    def total_bunga(self):
        if self.dana_bank and self.suku_bunga:
            return self.dana_bank * Decimal(self.suku_bunga / 100)
        return Decimal('0.00')

    def cicilan_per_bulan(self, tahun=5):
        if self.dana_bank:
            total_pinjaman = self.dana_bank + self.total_bunga()
            return total_pinjaman / Decimal(tahun * 12)
        return Decimal('0.00')

    def total_biaya_service(self):
        total = self.service_set.aggregate(Sum('biaya'))['biaya__sum']
        return total or Decimal('0.00')

    def hpp(self):
        total_pinjaman = (self.dana_bank or Decimal('0.00')) + self.total_bunga()
        if total_pinjaman == 0:
            return self.harga_pasar + self.total_biaya_service()
        return (self.harga_pasar / total_pinjaman) + self.total_biaya_service()


class Service(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    tanggal = models.DateField(default=timezone.now)
    deskripsi = models.TextField()
    biaya = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.car} - {self.tanggal}"
