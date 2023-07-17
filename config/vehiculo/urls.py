from django.contrib import admin
from django.urls import path
from .views import index, menu_view

urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu_view, name='menu'),
]
