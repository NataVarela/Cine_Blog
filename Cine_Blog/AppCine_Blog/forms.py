from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class editar_usuario_forms(UserCreationForm):
    email= forms.EmailField(label='modificar email')
    password1=forms.CharField(label='contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='repetir contraseña',widget=forms.PasswordInput)
    first_name= forms.CharField(label='Nombre')
    last_name= forms.CharField(label='Apellido')

class meta:
    models= User
    fields=['email','password1','password2','first_name','last_name']
    help_test={k:"" for  k in  fields} 