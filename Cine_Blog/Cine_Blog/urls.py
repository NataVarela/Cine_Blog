"""Cine_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from AppCine_Blog.views import categoria_accion
from AppCine_Blog.views import categoria_comedia
from AppCine_Blog.views import categoria_terror
from AppCine_Blog.views import categoria_aventura
from AppCine_Blog.views import categoria_thriller
from AppCine_Blog.views import datos_Hombre_Araña
from AppCine_Blog.views import inicio
from AppCine_Blog.views import Sobre_Nosotros
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio,name= "Inicio"),
    path('sobre_nosotros/',Sobre_Nosotros, name= "Sobre Nosotros"),
    path('Hombre_Araña/', datos_Hombre_Araña, name= "Hombre Araña"),
    path('C_accion/',categoria_accion, name= "Accion" ),
    path('C_comedia/',categoria_comedia,name= "Comedia" ),
    path('C_terror/',categoria_terror, name= "Terror" ),
    path('C_aventura/',categoria_aventura, name= "Aventura"),
    path('C_thriller/',categoria_thriller, name= "Thriller") ,
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)