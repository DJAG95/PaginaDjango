from django.forms import ModelForm
from vehiculos.models import usuario
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# Creamos los formularios
class usuarioForm(forms.Form):
	nombre = forms.CharField(max_length = 30)
	apellidos = forms.CharField(max_length = 50)
	dni = forms.CharField(max_length = 9)
	username = forms.CharField(max_length = 30)
	password = forms.CharField(widget=forms.PasswordInput, max_length = 30)
	edad = forms.IntegerField()
	correo = forms.CharField(max_length = 50)
	foto = forms.ImageField(required=False, widget=forms.FileInput)
		
class DireccionForm(forms.Form):
	calle = forms.CharField(max_length = 50)
	provincia = forms.CharField(max_length = 9)
	localidad = forms.CharField(max_length = 30)
	pais = forms.CharField(max_length = 50)
		
class formContacto(forms.Form):
	nombre = forms.CharField(max_length = 50)
	motivo = forms.ChoiceField(choices=(('Pass olvidada','Olvidé la contraseña',),('Financiacion','Plan de financiación',),('Consulta general','Consulta general',),('Problema plataforma','Informe de un problema relacionado con la web',)))
	correo = forms.EmailField(max_length = 50)
	mensaje = forms.CharField(max_length = 400)

class formConfiguracion(forms.Form):
	color = forms.ChoiceField(choices=(('Rojo','Rojo',),('Blanco','Blanco',),('Verde','Verde',),('Negro','Negro',)))
	tipo_paquete = forms.ChoiceField(choices=(('Sport','Sport',),('Confort','Confort',),('Senior','Senior',),('Basic','Basic',)))