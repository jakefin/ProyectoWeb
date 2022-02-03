#from curses.ascii import HT
import http
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from django.shortcuts import render
from django import *
# Create your views here.


def inicio(request):
    return render(request,"AppCoder/inicio.html")
    
def cursos(request):
    return render(request,"AppCoder/cursos.html")
    
def profesores(request):
    return HttpResponse('Inicio')
def estudiantes(request):
    return HttpResponse('Inicio')
def entregables(request):
    return HttpResponse('Inicio')