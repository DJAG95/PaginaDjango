from django.db import models
from django.contrib.auth.models import User

class fabricante(models.Model):
	nombre = models.CharField(max_length = 20)
	director = models.CharField(max_length = 20)
	logo = models.ImageField(upload_to = 'img/fabricante/', default='img/fabricante/marca.png')

	def __str__(self):
		return 'Fabricante: '+self.nombre+' Director: '+self.director

class vehiculo(models.Model):
	nombre = models.CharField(max_length = 20)
	n_ruedas = models.PositiveSmallIntegerField()
	potencia = models.PositiveSmallIntegerField()
	id_fabricante = models.ForeignKey(fabricante, on_delete=models.CASCADE)
	n_asientos = models.PositiveSmallIntegerField()
	n_puertas = models.PositiveSmallIntegerField()
	anyo_salida = models.PositiveSmallIntegerField()
	precio = models.FloatField(max_length = 8)
	foto = models.ImageField(upload_to = 'img/coches/', default='img/coches/coche.png')

	def __str__(self):
		return ('Modelo: '+self.nombre+', Número de ruedas: '+str(self.n_ruedas)+' Potencia (en KW): '+str(self.potencia)+' fabricante: '+self.id_fabricante.nombre+' número de asientos: '+str(self.n_asientos)+' Número de puertas '+str(self.n_puertas)+' año de salida: '+str(self.anyo_salida)+' precio: '+str(self.precio)+'')



class usuario(models.Model):
	id_user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
	nombre = models.CharField(max_length = 30)
	dni = models.CharField(max_length = 9, unique=True)
	edad = models.PositiveSmallIntegerField()
	apellidos = models.CharField(max_length = 50)
	correo = models.CharField(max_length = 50)
	foto = models.ImageField(upload_to = 'fotos/', default='fotos/user.png')

	def __str__(self):
		return 'DNI: '+self.dni+' nombre: '+self.nombre+' apellidos: '+self.apellidos+' con '+str(self.edad)+' años de edad y con correo: '+self.correo

class ejemplar(models.Model):
	vehiculo = models.ForeignKey(vehiculo, on_delete=models.CASCADE)
	color = models.CharField(max_length = 20)
	tipo_paquete = models.CharField(max_length = 40)

	def __str__(self):
		return 'Vehículo: '+self.vehiculo.nombre+' de color '+self.color+' y con el paquete '+self.tipo_paquete

class tiene_ejemplar(models.Model):
	ejemplar = models.ForeignKey(ejemplar, on_delete=models.CASCADE)
	usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

	def __str__(self):
		return 'El usuario '+self.usuario.nombre+' posee un '+self.ejemplar.vehiculo.nombre

class direccion(models.Model):
	usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
	calle = models.CharField(max_length = 30)
	provincia = models.CharField(max_length = 30)
	pais = models.CharField(max_length = 20)
	localidad = models.CharField(max_length = 40)

	def __str__(self):
		return 'El usuario '+self.usuario.nombre+' vive en la calle '+self.calle+' en '+self.localidad+', '+self.provincia+' en '+self.pais
		
		
		
