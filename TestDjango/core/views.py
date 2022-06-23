from django.shortcuts import render
from .models import Vehiculo

# Create your views here.
def home(request):    
    datos = {'vehiculos':Vehiculo.objects.all()}
    return render(request, 'core/home.html', datos)