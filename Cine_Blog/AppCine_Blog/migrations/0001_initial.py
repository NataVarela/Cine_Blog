# Generated by Django 4.0.4 on 2022-05-02 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.CharField(max_length=50, verbose_name='accion')),
                ('comedia', models.CharField(max_length=50, verbose_name='comedia')),
                ('terror', models.CharField(max_length=50, verbose_name='accion')),
                ('suspenso', models.CharField(max_length=50, verbose_name='accion')),
                ('aventura', models.CharField(max_length=50, verbose_name='accion')),
                ('thriller', models.CharField(max_length=50, verbose_name='thriller')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='apellido')),
                ('email', models.EmailField(max_length=254)),
                ('contra', models.CharField(max_length=10, verbose_name='contraseña')),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='titulo')),
                ('sinopsis', models.CharField(max_length=20, verbose_name='sinopsis')),
                ('imagen', models.ImageField(upload_to='')),
                ('fecha_estreno', models.DateField(verbose_name='fecha de estreno')),
                ('duracion', models.IntegerField(verbose_name='duracion')),
                ('trailer_link', models.CharField(max_length=256, verbose_name='trailer')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCine_Blog.categoria')),
            ],
        ),
    ]
