from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Pelicula


def inicio(request):

     return render (request,'inicio.html')

def Sobre_Nosotros(request):

     return render (request,'sobre_nosotros.html')

############## PELICULAS #################
def datos_Hombre_Araña(request):
     datos_H_A= Pelicula.objects.filter(titulo='Hombre Araña')
     contexto={"Hombre_Araña":datos_H_A }
     
     return render(request, "Hombre_Araña.html", contexto) 
     
############## CATEGORIAS #################
def categoria_accion(request):
     datos_accion= Pelicula.objects.filter(categoria='1')
     contexto={"datos_accion":datos_accion }
     return render(request, "C_accion.html", contexto)

def categoria_comedia(request):
     datos_comedia= Pelicula.objects.filter(categoria='3')
     contexto={"datos_comedia":datos_comedia }
     return render(request, "C_comedia.html", contexto)

def categoria_terror(request):
     datos_terror= Pelicula.objects.filter(categoria='5')
     contexto={"datos_terror":datos_terror }
     return render(request, "C_terror.html", contexto)

def categoria_aventura(request):
     datos_aventura= Pelicula.objects.filter(categoria='2')
     contexto={"datos_aventura":datos_aventura }
     return render(request, "C_aventura.html", contexto)

def categoria_thriller(request):
     datos_thriller= Pelicula.objects.filter(categoria='4')
     contexto={"datos_thriller":datos_thriller }
     return render(request, "C_thriller.html", contexto)