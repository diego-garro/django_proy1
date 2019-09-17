#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

path = '/home/diego/Documentos/Developer/Python/django/django_proy1/Proyecto1/plantillas/{}'

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): # Primera vista
    p1 = Persona("Profesor Diego", "Molina")
    fecha_actual = datetime.datetime.now()
    temas_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    #doc_externo = open(path.format('saludo.html'), 'r')
    #plt = Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo = get_template('saludo.html')
    #ctx = Context({"nombre" : p1.nombre, "apellido" : p1.apellido, "fecha": fecha_actual, "temas" : temas_curso})
    dicc = {"nombre" : p1.nombre, "apellido" : p1.apellido, "fecha": fecha_actual, "temas" : temas_curso}
    #documento = doc_externo.render(dicc)
    return render(request, "saludo.html", dicc)

def despedida(request):
    return HttpResponse("Hasta luego alumnos de Django!")

def dame_fecha(request):
    fecha_actual = datetime.datetime.now()
    respuesta = """<html>
        <body>
            <h1>
                Fecha y hora actuales: {}.
            </h1>
        </body>
    </html>
    """.format(fecha_actual)
    return HttpResponse(respuesta)

def calcula_edad(request, edad, anio):
    #edad_actual = 18
    periodo = anio - 2019
    edad_futura = edad + periodo
    respuesta = """<html>
        <body>
            <h1>
                En el año {} tendrás {} años!!
            </h1>
        </body>
    </html>
    """.format(anio, edad_futura)
    return HttpResponse(respuesta)
