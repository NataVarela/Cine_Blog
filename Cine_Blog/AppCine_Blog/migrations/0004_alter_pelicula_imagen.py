# Generated by Django 4.0.4 on 2022-05-03 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCine_Blog', '0003_alter_pelicula_sinopsis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(upload_to='media/'),
        ),
    ]