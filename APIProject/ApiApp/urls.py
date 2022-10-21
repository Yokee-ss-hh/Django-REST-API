from django.contrib import admin
from django.urls import path, include

from .views import drinks_list, drink_in_detail, add_new_drink, update_drink, delete_drink

urlpatterns = [
    path('drinks_list/', drinks_list, name='drinks_list'),
    path('drink_in_detail/<int:pk>/', drink_in_detail, name='drink_in_detail'),
    path('add_new_drink/', add_new_drink, name='add_new_drink'),
    path('update_drink/<int:pk>/', update_drink, name='update_drink'),
    path('delete_drink/<int:pk>/', delete_drink, name='delete_drink'),
]



