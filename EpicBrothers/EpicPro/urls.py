from django.urls import path, include
from EpicPro import views 
from .views import juegos, agregar, listar, modificar, eliminar, registro,JuegosViewset, error_facebook
from rest_framework import routers

router = routers.DefaultRouter()
router.register('juegos', JuegosViewset)


urlpatterns = [

    path('',views.home, name="Home"),
    path('servicios',views.servicios, name="Servicios"),
    path('tienda',views.tienda, name="Tienda"),
    path('blog',views.blog, name="Blog"),
    path('contacto',views.contacto, name="Contacto"),
    path('juegos',views.juegos, name="Juegos"),
    path('agregar', agregar, name="agregar" ),
    path('listar', listar, name="listar" ),
    path('modificar/<id>/', modificar, name="modificar" ),
    path('eliminar/<id>/', eliminar, name="eliminar" ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('error-facebook/', error_facebook, name="error_facebook"),
    
    
]