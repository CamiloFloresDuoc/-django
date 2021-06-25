from django.urls import path
from .views import index, contacto, listarVehiculos, agregarvehiculo, editarVehiculo, eliminarVehiculo

urlpatterns = [
    path('',index,name="index"),
    path('contacto/',contacto,name="contacto"),
    path('vehiculos/listar',listarVehiculos, name="listarVehiculos"),
    path('agregarvehiculo/',agregarvehiculo, name="agregarvehiculo"),
    path('Vehiculo/editar/<id>',editarVehiculo, name="editarVehiculo"),
    path('Vehiculo/eliminar/<id>',eliminarVehiculo, name="eliminarVehiculo"),
    
]