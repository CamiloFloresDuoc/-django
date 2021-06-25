from django.contrib import admin
from .models import Categoria, Vehiculo #aca las clases que cree

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Vehiculo)