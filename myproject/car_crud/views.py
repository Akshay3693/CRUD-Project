from django.shortcuts import render, redirect, get_object_or_404
from .models import Car

# Create your views here.
# car_crud/views.py

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_crud/car_list.html', {'cars': cars})

def add_car(request):
    if request.method == 'POST':
        car = Car(
            car_name=request.POST['car_name'],
            mfg_year=request.POST['mfg_year'],
            fuel_type=request.POST['fuel_type'],
            transmission=request.POST['transmission'],
            kms_driven=request.POST['kms_driven'],
            owners=request.POST['owners'],
            price=request.POST['price']
        )
        car.save()
        return redirect('car_list')
    return render(request, 'car_crud/add_car.html')

def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.car_name = request.POST['car_name']
        car.mfg_year = request.POST['mfg_year']
        car.fuel_type = request.POST['fuel_type']
        car.transmission = request.POST['transmission']
        car.kms_driven = request.POST['kms_driven']
        car.owners = request.POST['owners']
        car.price = request.POST['price']
        car.save()
        return redirect('car_list')
    return render(request, 'car_crud/update_car.html', {'car': car})

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    return redirect('car_list')