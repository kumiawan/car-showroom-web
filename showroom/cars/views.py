from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Car, Service
from .forms import CarForm, ServiceForm

def add_car(req):
    if req.method == 'POST':
        form = CarForm(req.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(req, 'Mobil berhasil ditambahkan! :D')
                return redirect('car_list')
            except Exception as e:
                messages.error(req, f'Gagal menyimpan data mobil: {e}')
    else:
        form = CarForm()
    return render(req, 'cars/add_car.html', {'form': form})

def car_detail(req, pk):
    try:
        car = Car.objects.get(pk=pk)
        services = Service.objects.filter(car=car).order_by('-tanggal')
        return render(req, 'cars/car_detail.html', {
            'car': car,
            'services': services
        })
    except Car.DoesNotExist:
        messages.error(req, 'Mobil tidak ditemukan :(')
        return redirect('car_list')  
    except Exception as e:
        messages.error(req, f'Gagal memuat detail mobil: {e}')
        return redirect('car_list')

def car_list(req):
    try:
        cars = Car.objects.all()  
        return render(req, 'cars/car_list.html', {'cars': cars})
    except Exception as e:
        messages.error(req, f'Tidak bisa mengambil daftar mobil: {e}')
        return render(req, 'cars/car_list.html', {'cars': []})

def add_service(req, pk):
    try:
        car = get_object_or_404(Car, pk=pk)
        if req.method == 'POST':
            form = ServiceForm(req.POST)
            if form.is_valid():
                service = form.save(commit=False)
                service.car = car
                service.save()
                messages.success(req, 'Service berhasil ditambahkan!')
                return redirect('car_detail', pk=car.pk)
        else:
            form = ServiceForm()
        return render(req, 'cars/add_service.html', {'form': form, 'car': car})
    except Exception as e:
        messages.error(req, f'Terjadi kesalahan saat menambahkan service: {e}')
        return redirect('car_detail', pk=pk)

def delete_car(req, pk):
    try:
        car = get_object_or_404(Car, pk=pk)
        car.delete()
        messages.success(req, f'Mobil {car.merk} {car.model} berhasil dihapus!')
    except Exception as e:
        messages.error(req, f'Tidak bisa menghapus mobil: {e}')
    return redirect('car_list')
