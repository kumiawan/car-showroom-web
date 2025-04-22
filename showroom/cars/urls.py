# cars/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),  
    path('tambah-mobil/', views.add_car, name='add_car'),  
    path('mobil/<int:pk>/', views.car_detail, name='car_detail'),  
    path('mobil/<int:pk>/tambah-service/', views.add_service, name='add_service'), 

]
