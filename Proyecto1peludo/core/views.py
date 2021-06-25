from django import forms
from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def contacto(request):
    return render(request,'core/contacto.html')

def listarVehiculos(request):
    vehiculos = Vehiculo.objects.all()

    datos = {
        'vehiculos' : vehiculos
    }
    return render(request,'core/listarVehiculos.html',datos)

def agregarvehiculo(request):

    datos = {
        'form' : VehiculoForm()
    }

    if request.method == 'POST':
        formulario = VehiculoForm(request.POST) #extraer patente ver metodo request por post traer ese dato en documentacion

        vehiculo = Vehiculo.objects.get(patente = id)
        todos = vehiculos.objects.all()

        if todos.filter(id=vehiculo.id).exists():
            datos['mensaje'] = 'Patente ya existe'

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'vehiculo agregado exitosamente'

    return render(request,'core/agregarvehiculo.html',datos)

def editarVehiculo(request,id):

    vehiculo = Vehiculo.objects.get(patente = id)

    datos = {
        'form' : VehiculoForm(instance=vehiculo)
    }

    if request.method == 'POST':
        formulario = VehiculoForm(data=request.POST,instance=vehiculo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Datos modificados exitosamente'
    return render(request, 'core/editarVehiculo.html',datos)


def eliminarVehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect(to="listarVehiculos")