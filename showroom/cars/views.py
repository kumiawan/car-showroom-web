from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import CarForm
from .forms import ServiceForm
from .models import Car, Service

def add_car(req):
    if req.method == 'POST':
        form = CarForm(req.POST)
        if form.is_valid():
            new_car = form.save()
            messages.success(req, 'Mobil berhasil ditambahkan! :D')
            return redirect('car_list')  
    else:
        form = CarForm()
    return render(req, 'cars/add_car.html', {'form': form})

def car_detail(req, pk):
    try:
        car = Car.objects.get(pk=pk)
        services = Service.objects.filter(car=car).order_by('-tanggal')
    except Car.DoesNotExist:
        messages.error(req, 'Mobil tidak ditemukan :(')
        return redirect('car_list')  
    
    return render(req, 'cars/car_detail.html', {
        'car': car,
        'services': services
        })

def car_list(req):
    cars = Car.objects.all()  
    return render(req, 'cars/car_list.html', {'cars': cars})

def add_service(req, pk):
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
