from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car-detail/<int:pk>/', views.car_detail, name='car_detail'),
    path('add-car/', views.add_car, name='add_car'),
    path('delete-car/<int:pk>/', views.delete_car, name='delete_car'), 
    path('mobil/<int:pk>/tambah-service/', views.add_service, name='add_service'),
]
