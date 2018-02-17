from django.contrib import admin
from django.urls import path
from vehiculos import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	
	path('index/',views.Principal.as_view()),


	path('logout/',views.logout_view,name='logout'),
	path('ventajas/',views.Ventajas.as_view()),
	path('contacto/',views.contacto,name='contacto'),
	path('usuario/', views.verUsuario,name='VerUsuario'),
	path('perfil/usuario_coche/', views.ejemplarUsuario,name='ejemplarUsuari'),
	path('fabricante_Coches/<str:marca>', views.fabricanteCoche,name='fabricantecoche'),
	path('perfil/', views.perfil,name='perfiluser'),
	path('registro/', views.registro,name='hacerRegistro'),
	path('nuevaDireccion/', views.registroDireccion,name='nuevaDireccion'),
	path('personalizacion/<str:nombre>', views.personalizacion,name='personalizacion'),
	path('compartir/<str:nombre>', views.compartir,name='compartir'),



	path('acerca/',views.AcercaView.as_view()),
	path('lisviewusuarios/',views.EmpleadoList.as_view()),
	path('concesionario/',views.concesionario,name='concesionario'),
	path('concesionario/<str:marca>', views.concesionarioPorFabricante,name='concesionarioPorFabricante'),
	path('login/',login,{'template_name':'login.html',},name='InicioSesion'),


]