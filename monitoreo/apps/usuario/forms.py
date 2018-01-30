from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import models


class UsuarioForm(UserCreationForm):


	class Meta: 
		model = User

		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			
			
			
		]
		labels = {
			'username' : 'Usuario',
			'first_name' : 'Nombre',
			'last_name' : 'Apellido',
			'email' : 'Correo',

		
		}

		widgets = {
			'username' : forms.TextInput(attrs={'class' : 'form-control'}),
			'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
			'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
			'email' : forms.TextInput(attrs={'class' : 'form-control'}),
			'password1' : forms.TextInput(attrs={'class' : 'form-control'}),
			'password2' : forms.TextInput(attrs={'class' : 'form-control'}),
			
		}

		
		