from django.contrib import admin
from django.urls import path
from .views import index, menu_view,catalogo_view,logout_view, login_view, register_view, datosform_view, vehiculoform_view, gracias_view

urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu_view, name='menu'),
    path('catalogo/', catalogo_view, name='catalogo'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('datosform/', datosform_view, name='datosform'),
    path('add/', vehiculoform_view, name='vehiculoform'),
    path('thanks/', gracias_view, name='gracias'),
]
