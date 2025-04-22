from django import forms
from django.forms import DateInput
from .models import Car
from .models import Service

class CarForm(forms.ModelForm):
    dibeli_dengan_bank = forms.BooleanField(required=False, label="Dibeli via Bank?")

    class Meta():
        """docstring for Meta."""
        model = Car
        fields = ['merk', 'model', 'tahun', 'harga_pasar', 'dana_bank', 'suku_bunga']

        def __init__(self, *args, **kwargs):
            super(CarForm, self).__init__(*args, **kwargs)
            self.fields['dana_bank'].widget.attrs.update({'class' : 'bank-field'})
            self.fields['suku_bunga'].widget.attrs.update({'class' : 'bank-field'})

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['tanggal', 'deskripsi', 'biaya']
        widgets = {
                'tanggal': DateInput(attrs={'type':'date'})
                }

