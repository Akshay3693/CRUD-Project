from django.urls import path
from .views import car_list, add_car, update_car, delete_car

urlpatterns = [
    path('', car_list, name='car_list'),
    path('add/', add_car, name='add_car'),
    path('update/<int:car_id>/', update_car, name='update_car'),
    path('delete/<int:car_id>/', delete_car, name='delete_car'),
]