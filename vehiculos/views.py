from django.shortcuts import render
from vehiculos.models import usuario, ejemplar, direccion, vehiculo, tiene_ejemplar, fabricante
from django.http import Http404, HttpResponseRedirect, HttpResponse
from vehiculos.forms import usuarioForm, formContacto, DireccionForm, formConfiguracion, formCompartir
from django.views.generic import TemplateView, ListView
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.core.mail import EmailMessage
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages



class Principal(TemplateView):
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		total_usuarios = len(usuario.objects.all())
		total_vehiculos = len(vehiculo.objects.all())
		total_fabricantes = len(fabricante.objects.all())
		context = {'total_usuarios':total_usuarios, 'total_vehiculos':total_vehiculos, 'total_fabricantes':total_fabricantes}
		return (context)
	template_name = "index.html"

class concesionario(TemplateView):
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		lista_fabricantes = fabricante.objects.order_by('nombre')
		lista_vehiculos = vehiculo.objects.order_by('nombre')
		total_vehiculos = len(lista_vehiculos)
		context = {'lista_fabricantes':lista_fabricantes, 'lista_vehiculos':lista_vehiculos, 'total_vehiculos':total_vehiculos}
		return (context)
	template_name = "concesionario.html"

@method_decorator(login_required, name='dispatch')
class contacto(TemplateView):
	def get(self,request):
		form=formContacto()
		return render(request, 'contacto.html', {'form': form})

	def post(self, request):
		form = formContacto(request.POST)
		if form.is_valid():
			asunto = 'Round-Robin.com - '+form.cleaned_data['motivo']
			mensaje = ' Correo enviado por: '+form.cleaned_data['nombre']+'\n\nCon el correo: '+form.cleaned_data['correo']+'\n\n\nEl mensaje es el siguiente: '+form.cleaned_data['mensaje']
			mail = EmailMessage(asunto, mensaje, to=['round.robin.cc@gmail.com'])
			mail.send()
			messages.add_message(request, messages.SUCCESS, 'Gracias por contactar con nosotros, uno de nuestros agentes les responderá con la mayor brevedad posible')
		return render(request, 'contacto.html', {'form': form})

class registro(TemplateView):
	def get(self,request):
		form=usuarioForm()
		return render(request,'registro.html',{'form':form})
	def post(self,request):
		form=usuarioForm(request.POST,request.FILES)
		if form.is_valid():
			us_username = form.cleaned_data['username']
			us_pass = form.cleaned_data['password']
			u_nombre = form.cleaned_data['nombre']
			u_dni = form.cleaned_data['dni']
			u_edad = form.cleaned_data['edad']
			u_apellidos = form.cleaned_data['apellidos']
			u_correo = form.cleaned_data['correo']
			u_foto = form.cleaned_data['foto']
			usern = User(username=us_username)
			usern.set_password(us_pass)
			usern.save()
			usuario2 = usuario(id_user=usern,nombre=u_nombre, dni=u_dni,edad=u_edad,apellidos=u_apellidos,correo=u_correo, foto=u_foto)
			usuario2.save()
			messages.add_message(request, messages.SUCCESS, 'Bienvenido a la familia Round-Robin.com '+u_nombre)
		return HttpResponseRedirect("/vehiculos/perfil")


class Ventajas(TemplateView):
    template_name = "ventajas.html"



def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Se ha deslogueado con éxito')
    return HttpResponseRedirect('/vehiculos/index')





def concesionarioPorFabricante(request, marca):
	try:
		lista_fabricantes = fabricante.objects.order_by('nombre')
		fabricantep = fabricante.objects.get(nombre = marca)
		lista_vehiculos = vehiculo.objects.filter(id_fabricante = fabricantep.pk)
	except Exception as e:
		return HttpResponseRedirect('/vehiculos/concesionario')
	context = {'lista_fabricantes':lista_fabricantes,'lista_vehiculos':lista_vehiculos, 'marca':fabricantep}
	return render(request,'concesionarioFab.html', context)


@login_required
def ejemplarUsuario(request):
	if request.method == 'POST':
		form=formCompartir(request.POST,request.FILES)
		if form.is_valid():
			try:
				ejemplar3 = form.cleaned_data['id_ejemplar']
				dniU = form.cleaned_data['dni']
				ejemplar2 = ejemplar.objects.get(pk=ejemplar3)
				usuarioActual = usuario.objects.get(dni = dniU)
				tiene_ejemplar2 = tiene_ejemplar(ejemplar=ejemplar2, usuario=usuarioActual)
				tiene_ejemplar2.save()
				messages.add_message(request, messages.SUCCESS, 'Su vehículo ha sido compartido correctamente.')
				return HttpResponseRedirect("..")
			except Exception as e:
				messages.add_message(request, messages.ERROR, 'Este usuario no existe, su vehículo no ha sido compartido con nadie')
				return HttpResponseRedirect("..")
			
	else:
		form=formCompartir()
	try:
		usuariop = usuario.objects.get(id_user = request.user.pk)
		lista_vehiculos = tiene_ejemplar.objects.filter(usuario = usuariop.pk)
	except Exception as e:
		raise e
	context = {'usuario':usuariop, 'lista_vehiculos':lista_vehiculos, 'form':form}
	return render(request,'ejemplarUsuario.html', context)


@login_required
def personalizacion(request, nombre):
	if request.method == 'POST':
		form=formConfiguracion(request.POST,request.FILES)
		if form.is_valid():
			color = form.cleaned_data['color']
			tipo_paquete = form.cleaned_data['tipo_paquete']
			vehiculoActual = vehiculo.objects.get(pk = nombre)
			ejemplar2 = ejemplar(vehiculo=vehiculoActual, color=color, tipo_paquete=tipo_paquete)
			ejemplar2.save()
			usuarioActual = usuario.objects.get(id_user = request.user.pk)
			tiene_ejemplar2 = tiene_ejemplar(ejemplar=ejemplar2, usuario=usuarioActual)
			tiene_ejemplar2.save()
			messages.add_message(request, messages.SUCCESS, 'Uno de nuestros agentes se pondrá en contacto con usted en breve, por motivos de corrección de la web, este vehículo ya aparece en su sección de vehículos')
			return HttpResponseRedirect("../perfil")
	else:
		form=formConfiguracion()
	try:
		vehiculoS = vehiculo.objects.get(pk = nombre)
	except Exception as e:
		raise e
	context = {'c': vehiculoS, 'form':form}
	return render(request,'personalizado.html', context)


def perfil(request):
	if request.user.is_authenticated:
		try:
			usuariop = usuario.objects.get(id_user = request.user.pk)
			direcciones = direccion.objects.filter(usuario = usuariop.pk)
		except Exception as e:
			raise e
		context = {'u':usuariop, 'd':direcciones}
		return render(request,'perfil.html', context)
	else:
		return HttpResponseRedirect("../registro")

@login_required
def registroDireccion(request):
	if request.method == 'POST':
		form=DireccionForm(request.POST,request.FILES)
		if form.is_valid():
			calle = form.cleaned_data['calle']
			provincia = form.cleaned_data['provincia']
			localidad = form.cleaned_data['localidad']
			pais = form.cleaned_data['pais']
			usuarioA = usuario.objects.get(id_user = request.user.pk)
			direccion2 = direccion(usuario=usuarioA,calle=calle, provincia=provincia, localidad=localidad, pais=pais)
			direccion2.save()
			messages.add_message(request, messages.SUCCESS, 'Su nueva drección se ha registrado correctamente')
			return HttpResponseRedirect("../perfil")
	else:
		form=DireccionForm()		
	return render(request,'registroDireccion.html',{'form':form})



	
