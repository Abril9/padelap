from django.urls import path
from django.conf.urls import url, include
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()
# define the router path and viewset to be used
router.register(r'registrar', UsuarioViewSet) 
router.register(r'registrar_jugador', JugadorViewSet) 
router.register(r'nuevo_torneo', TorneoViewSet) 
router.register(r'nuevo_partido', PartidoViewSet) 

urlpatterns = [

    #devuelve el usuario correpsndiente si fue correcta la password
    path('login/<str:username>/<str:password>', login, name='login'), 


    path('', bienvenido, name='bienvenido'),
    path('usuarios/', usuarios_json, name='usuarios_json'),
    path('torneos/', torneos_json, name='torneos_json'),
    path('partidos/', partidos_json, name='partidos_json'),
    
    # devuelve el torneo y los partidos que tiene asociados 
    path('torneo_partidos/<int:id>', torneo_partidos_json, name='partidos_json'), 
    
    # devuelve todos los partidos del jugador con el id que mandaron
    path('partidos_usuario/<int:id>', resultados_usuario, name='partidos_usuario'), 

    path('torneos_organiza_usuario/<int:id>', torneos_organiza_usuario, name='torneos_organiza_usuario'), 
    path('id_usuario_x_username/<str:username>', id_usuario_x_username, name='id_usuario_x_username'), 
    path('inscribir_jugador_partido/', inscribir_jugador_partido, name='inscribir_jugador_partido'), 
    path('act_categoria/', act_categoria, name='act_categoria'), 

    url(r'^', include(router.urls)),
    url(r'^/registrar/', include('rest_framework.urls', namespace= 'rest_framework_registrar')),
    url(r'^/registrar_jugador/', include('rest_framework.urls', namespace= 'rest_framework_reg_jug')),
    url(r'^/nuevo_torneo/', include('rest_framework.urls', namespace= 'rest_framework_nuev_torn')),
    url(r'^/nuevo_partido/', include('rest_framework.urls', namespace= 'rest_framework_nuev_part')),
]