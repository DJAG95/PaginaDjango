from django.shortcuts import render
from vehiculos.models import usuario, ejemplar, direccion, vehiculo, tiene_ejemplar, fabricante
from django.http import Http404, HttpResponseRedirect, HttpResponse
from vehiculos.forms import usuarioForm, formContacto, DireccionForm, formConfiguracion
from django.views.generic import TemplateView, ListView
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth import logout
from django.contrib.auth.models import User


class Principal(TemplateView):
    template_name = "index.html"

class Ventajas(TemplateView):
    template_name = "ventajas.html"

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/vehiculos/index')


def contacto(request):
    if request.method == 'POST':
        form = formContacto(request.POST)
        if form.is_valid():
        	asunto = 'Round-Robin.com - '+form.cleaned_data['motivo']
        	mensaje = ' Correo enviado por: '+form.cleaned_data['nombre']+'\n\nCon el correo: '+form.cleaned_data['correo']+'\n\n\nEl mensaje es el siguiente: '+form.cleaned_data['mensaje']
        	mail = EmailMessage(asunto, mensaje, to=['round.robin.cc@gmail.com'])
        	mail.send()
        return HttpResponseRedirect('/vehiculos/index')
    else:
        form = formContacto()
    return render(request, 'contacto.html', {'form': form})

def concesionario(request):
	lista_fabricantes = fabricante.objects.order_by('nombre')
	lista_vehiculos = vehiculo.objects.order_by('nombre')
	total_vehiculos = len(lista_vehiculos)
	context = {'lista_fabricantes':lista_fabricantes, 'lista_vehiculos':lista_vehiculos, 'total_vehiculos':total_vehiculos}
	return render(request,'concesionario.html', context)

def concesionarioPorFabricante(request, marca):
	try:
		lista_fabricantes = fabricante.objects.order_by('nombre')
		fabricantep = fabricante.objects.get(nombre = marca)
		lista_vehiculos = vehiculo.objects.filter(id_fabricante = fabricantep.pk)
	except Exception as e:
		raise e
	context = {'lista_fabricantes':lista_fabricantes,'lista_vehiculos':lista_vehiculos, 'marca':fabricantep}
	return render(request,'concesionarioFab.html', context)

def verUsuario(request):
	lista_usuarios = usuario.objects.order_by('nombre')
	context = {'lista_usuarios':lista_usuarios}
	return render(request,'usuarios.html', context)

def ejemplarUsuario(request):
	try:
		usuariop = usuario.objects.get(id_user = request.user.pk)
		lista_vehiculos = tiene_ejemplar.objects.filter(usuario = usuariop.pk)
	except Exception as e:
		raise e
	context = {'usuario':usuariop, 'lista_vehiculos':lista_vehiculos}
	return render(request,'ejemplarUsuario.html', context)

def fabricanteCoche(request, marca):
	try:
		fabricantep = fabricante.objects.get(nombre = marca)
		vehiculop = vehiculo.objects.filter(id_fabricante = fabricantep.pk)
	except Exception as e:
		raise e
	context = {'vehiculo':vehiculop, 'marca':fabricantep}
	return render(request,'fabricanteCoche.html', context)

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
			return HttpResponseRedirect("../perfil")
	else:
		form=formConfiguracion()
	try:
		vehiculoS = vehiculo.objects.get(pk = nombre)
	except Exception as e:
		raise e
	context = {'c': vehiculoS, 'form':form}
	return render(request,'personalizado.html', context)

def compartir(request, ejemplar, usuario):
	if request.method == 'POST':
		form=formConfiguracion(request.POST,request.FILES)
		if form.is_valid():
			vehiculoActual = vehiculo.objects.get(pk = nombre)
			ejemplar2 = ejemplar(vehiculo=vehiculoActual, color=color, tipo_paquete=tipo_paquete)
			ejemplar2.save()
			usuarioActual = usuario.objects.get(id_user = request.user.pk)
			tiene_ejemplar2 = tiene_ejemplar(ejemplar=ejemplar2, usuario=usuarioActual)
			tiene_ejemplar2.save()
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
	try:
		usuariop = usuario.objects.get(id_user = request.user.pk)
		direcciones = direccion.objects.filter(usuario = usuariop.pk)
	except Exception as e:
		raise e
	context = {'u':usuariop, 'd':direcciones}
	return render(request,'perfil.html', context)


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
			return HttpResponseRedirect("../perfil")
	else:
		form=DireccionForm()		
	return render(request,'registroDireccion.html',{'form':form})

def registro(request):
	if request.method == 'POST':
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
			usern = User(username=us_username, password=us_pass)
			usern.save()
			usuario2 = usuario(id_user=usern,nombre=u_nombre, dni=u_dni,edad=u_edad,apellidos=u_apellidos,correo=u_correo, foto=u_foto)
			usuario2.save()
			return HttpResponseRedirect("/vehiculos\login")
	else:
		form=usuarioForm()		
	return render(request,'registro.html',{'form':form})

class AcercaView(TemplateView):
	template_name="acerca.html"

class EmpleadoList(ListView):
	model=usuario
	template_name='empleado_list.html'		
