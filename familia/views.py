from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Integrante

# Create your views here.
def base(request):
    return redirect(index)

def mostrar(request):
    data = {
        'data' : Integrante.objects.all(),
    }
    return render(request, 'mostrar.html', data)

def crear(request, dni : int = None, nombre : str = None, apellido = None):
    if (nombre == None or apellido == None or dni == None):
        return redirect(index)
    
    integrante = Integrante(nombre = nombre, apellido = apellido, dni = dni, alta = datetime.now())
    integrante.save()

    data = {
        'titulo' : 'Familiar creado',
        'subtitulo' : apellido + ', ' + nombre,
    }
    return render(request, 'crear.html', data)

def index(request):
    data = {
        'titulo' : 'Nuestro Primer MVT',
        'subtitulo' : 'Agenda Familiar',
    }
    return render(request, 'index.html', data)