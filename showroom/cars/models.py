from django.db import models
from django.utils import timezone

class Car(models.Model):
    merk = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    tahun = models.IntegerField()
    harga_pasar = models.DecimalField(max_digits=12, decimal_places=2)
    dana_bank = models.DecimalField(max_digits=12, decimal_places=2 , null=True, blank=True)
    suku_bunga = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.merk} {self.model} {self.tahun}"

    def total_bunga():
        if self.dana_bank and self.suku_bunga:
            return self.dana_bank * (self.suku_bunga / 100)
        return 0

    def cicilan_per_bulan(self, tahun=5):
        if self.dana_bank:
            total_pinjaman = self.dana_bank + self.total_bunga()
            return total_pinjaman / (tahun * 12)
        return 0

    def total_biaya_service(self):
        return sum(service.biaya for service in self.service_set.all())

    def hpp(self):
        bunga_total = self.total_bunga()
        pinjaman = self.dana_bank or 0
        return (self.harga_dasar / (pinjaman + bunga_total +1))

class Service(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    tanggal = models.DateField(default=timezone.now)
    deskripsi = models.TextField()
    biaya = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.car} - {self.tanggal}"
