#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Template, Context
import datetime

path = '/home/diego/Documentos/Developer/Python/django/Proyecto1/Proyecto1/plantillas/{}'

def saludo(request): # Primera vista
    doc_externo = open(path.format('saludo.html'), 'r')
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

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
