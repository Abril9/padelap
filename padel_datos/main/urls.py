from django.urls import path
from django.conf.urls import url, include
from .views import bienvenido,usuarios_json, torneos_json, partidos_json, torneo_partidos_json
from .views import UsuarioViewSet,TorneoViewSet, PartidoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
# define the router path and viewset to be used
router.register(r'registrar', UsuarioViewSet) 
router.register(r'nuevo_torneo', TorneoViewSet) 
router.register(r'nuevo_partido', PartidoViewSet) 

urlpatterns = [

    path('', bienvenido, name='bienvenido'),
    path('usuarios/', usuarios_json, name='usuarios_json'),
    path('torneos/', torneos_json, name='torneos_json'),
    path('partidos/', partidos_json, name='partidos_json'),
    
    # devuelve el torneo y los partidos que tiene asociados 
    path('torneo_partidos/<int:id>', torneo_partidos_json, name='partidos_json'), 
    url(r'^', include(router.urls)),
    url(r'^/registrar/', include('rest_framework.urls', namespace= 'rest_framework')),
    url(r'^/nuevo_torneo/', include('rest_framework.urls', namespace= 'rest_framework')),
    url(r'^/nuevo_partido/', include('rest_framework.urls', namespace= 'rest_framework')),
]