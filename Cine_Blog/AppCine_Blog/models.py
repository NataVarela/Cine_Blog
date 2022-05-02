from django.db import models


class Usuario(models.Model):
    nombre=models.CharField('nombre' , max_length=50)
    apellido=models.CharField('apellido' , max_length=20)
    email=models.EmailField()
    contra=models.CharField('contraseña' , max_length=10)


class Categoria(models.Model):
    accion= models.CharField('accion', max_length=50)
    comedia= models.CharField('comedia',max_length=50)
    terror= models.CharField('accion',max_length=50)
    suspenso= models.CharField('accion',max_length=50)
    aventura= models.CharField('accion',max_length=50)
    thriller= models.CharField('thriller',max_length=50)

class Pelicula(models.Model):
    titulo=models.CharField('titulo' , max_length=50)
    sinopsis=models.CharField('sinopsis' , max_length=20)
    imagen=models.ImageField()
    fecha_estreno=models.DateField('fecha de estreno' )
    duracion= models.IntegerField('duracion')
    trailer_link= models.CharField('trailer', max_length=256)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)