from django.contrib import admin
from django.urls import path
from vehiculos import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	
	path('index/',views.Principal.as_view()),
	path('ventajas/',views.Ventajas.as_view()),
	path('concesionario/',views.concesionario.as_view()),
	path('concesionario/<str:marca>', views.concesionarioPorFabricante,name='concesionarioPorFabricante'),
	path('registro/', views.registro.as_view()),
	path('perfil/', views.perfil,name='perfiluser'),
	path('personalizacion/<str:nombre>', views.personalizacion,name='personalizacion'),
	path('contacto/',views.contacto.as_view()),
	path('perfil/usuario_coche/', views.ejemplarUsuario,name='ejemplarUsuari'),
	path('nuevaDireccion/', views.registroDireccion,name='nuevaDireccion'),
	path('login/',login,{'template_name':'login.html',},name='InicioSesion'),
	

	path('logout/',views.logout_view,name='logout'),
	


]