from django.contrib import admin

# Register your models here.
from .models import Vehiculo

class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Vehiculo,VehiculoAdmin)