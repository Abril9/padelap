from django.urls import path
from .views import bienvenido,usuarios_json, crear_usuario, torneo

urlpatterns = [

    path('', bienvenido, name='bienvenido'),
    path('usuarios/', usuarios_json, name='usuarios_json'),
    path('crear/', crear_usuario, name='usuarios_json'),
    path('torneo/', torneo, name='torneo'),
]