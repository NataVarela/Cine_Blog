from django.contrib import admin
from .models import Usuario
from .models import Categoria
from .models import Pelicula
# Register your models here.

# class PeliculaAdmin(admin.ModelAdmin):    #VER PORQUE NO FUNCIONA!!!
#     list_display=['titulo','duracion']
#     search_fields=['titulo']

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Pelicula)