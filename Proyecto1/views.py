from django.http import HttpResponse
import datetime
from django.shortcuts import render 

def saludo(request):

    return HttpResponse("Hola alumnos")


def despedida(request):

    return HttpResponse("Hasta prnto!") 


    
def damefecha(request):

    fecha_actual=datetime.datetime.now()

    document="""<html>
    <body>
    <h2>
    La Fecha y hora actual %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(document)


def calculaEdad(request, edad, agno):

    periodo=agno-2021
    edadFutura=edad+periodo
    document="En el año {} tendrás {} años".format(agno, edadFutura)

    return HttpResponse(document)


class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido


def cursos(request):

    ahora=datetime.datetime.now()
    cursos = ["Programación I", "Programación II", "Bussines Inteligent", "AI Python"]
    p1=Persona("Juan", "Diaz")

    return render(
        request, 
        "template_01.html",
        {
        "nombre_persona":p1.nombre,
        "apellido_persona":p1.apellido,
        "fecha_actual":ahora,
        "cursos":cursos
         })