from django.http import HttpResponse
from datetime import datetime 
from django.template import Template
from django.template.context import Context
from django.template import loader

def hola(request):
    return HttpResponse("Hola")

def saludo(request):
    return HttpResponse("Pepe")

def hoy(request):
    hoy = datetime.now()
    return HttpResponse(f'Hoy es {hoy}')

def miNombreEs(request, nombre):
    return HttpResponse(f'Hola {nombre}')

def probandoTemplate(request):
    template_html = open('C:/Users/leona/Documents/ProyectoCoder/Web/Web/template/templates.html')
    template = Template(template_html.read())
    template_html.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)