from django.db.models import Model
from django.db.models.fields import CharField, IntegerField, EmailField,BooleanField, DateField

# Create your models here.

class Curso(Model):
    nombre = CharField(max_length=40)
    camada = IntegerField() # si no le pongo nada, el campo es obligatorio.

class Estudiante(Model):
    nombre= CharField(max_length=30)
    apellido= CharField(max_length=30)
    email= EmailField()

class Profesor(Model):
    nombre= CharField(max_length=30)
    apellido= CharField(max_length=30)
    email= EmailField()
    profesion= CharField(max_length=30)

class Entregable(Model):
    nombre= CharField(max_length=30)
    fechaDeEntrega = DateField()  
    entregado = BooleanField()


