#from curses.ascii import HT
import http
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
# Create your views here.

# def crear_curso(request, camada):
#     curso = Curso(nombre='Python', camada=camada)
#     curso.save()
#     return HTTPResponse(f'Curso Creado! {camada}')