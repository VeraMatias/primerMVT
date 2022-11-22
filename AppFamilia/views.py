from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
from django.template import loader

import datetime
 

# Create your views here.

def familiar(request):
    #Vista para crear registros de modelos Familiar()
    
    d1 = datetime.date(1993, 2, 11)
    f1 = Familiar(nombre = "Matias", edad = 29, fecha_nacimiento = d1)
    f1.save()

    d2 = datetime.date(1990, 9, 15)
    f2 = Familiar(nombre = "Silene", edad = 32, fecha_nacimiento = d2)
    f2.save()

    d3 = datetime.date(1965, 12, 5)
    f3 = Familiar(nombre = "Marta", edad = 56, fecha_nacimiento = d3)
    f3.save()

    cadena = "Familiares Creados"
    return HttpResponse(cadena)

def mostrar_familiares(request):
    #Aca leeriamos la base de datos pero por el momento creo un diccionario que lo reemplace.
    d1 = datetime.date(1993, 2, 11)
    d2 = datetime.date(1990, 9, 15)
    d3 = datetime.date(1965, 12, 5)
    diccionario = {"nombres": ["Matias", "Silene", "Marta"], "edades": [29,32,56], "fecha_nacimientos": [d1,d2,d3]}

    plantilla = loader.get_template('template_familiares.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)