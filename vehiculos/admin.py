from django.contrib import admin
from django.db import models
from vehiculos.models import vehiculo
from vehiculos.models import fabricante
from vehiculos.models import usuario
from vehiculos.models import ejemplar
from vehiculos.models import tiene_ejemplar
from vehiculos.models import direccion

admin.site.register(vehiculo)
admin.site.register(fabricante)
admin.site.register(usuario)
admin.site.register(ejemplar)
admin.site.register(tiene_ejemplar)
admin.site.register(direccion)
