from django.contrib import admin
from django import forms
from django.db import models
from django.contrib.auth.models import User
from vehiculos.models import vehiculo, fabricante, usuario, ejemplar, tiene_ejemplar, direccion


class ejemplarStacked(admin.StackedInline):
	model = ejemplar

class vehiculoSearch(admin.ModelAdmin):
	search_fields = ['nombre']
	ordering=['nombre']
	list_per_page=20
	list_filter=['id_fabricante']
	inlines = [ejemplarStacked,]


class usuarioValid(forms.ModelForm):
	def clean_edad(self):
		if (self.cleaned_data['edad'] < 18):
			raise forms.ValidationError("El usuario debe ser mayor de edad")
		else:
			return self.cleaned_data['edad']

class usuarioAdmin(admin.ModelAdmin):
	form=usuarioValid



admin.site.register(vehiculo,vehiculoSearch)
admin.site.register(fabricante)
admin.site.register(usuario, usuarioAdmin)
admin.site.register(ejemplar)
admin.site.register(tiene_ejemplar)
admin.site.register(direccion)