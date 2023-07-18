from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    options_marca = [
        ["Fiat", "Fiat"], 
        ["Chevrolet", "Chevrolet"],
        ["Ford", "Ford"],
        ["Toyota", "Toyota"],
    ]
    marca = models.CharField(max_length = 20, choices = options_marca, default="Fiat")
    modelo = models.CharField(max_length = 100)
    serial_carroceria = models.CharField(max_length = 50)
    serial_motor = models.CharField(max_length = 50)
    options = [
        ["Particular", "Particular"], 
        ["Transporte", "Transporte"],
        ["Carga", "Carga"],
    ]
    categoria = models.CharField(max_length = 20, choices = options, default="Particular")
    precio = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actuialización')
    
    class Meta:
        permissions = (
            ("visualizar_catalogo", "Listado de vehiculos"),
            ("add_vehiculomodel","Agregar vehiculo"),
            )
        verbose_name_plural = "Vehiculos"