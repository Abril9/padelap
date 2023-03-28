import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from itertools import chain
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt


from .models import Jugador, Resultado, Torneo, Usuario, Partido
from .serializers import UsuarioSerializer, PartidoSerializer, TorneoSerializer, JugadorSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all().order_by('id')
    serializer_class = JugadorSerializer


class TorneoViewSet(viewsets.ModelViewSet):
    queryset = Torneo.objects.all().order_by('id')
    serializer_class = TorneoSerializer

class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all().order_by('id')
    serializer_class = PartidoSerializer


def usuarios_json(request):
    qs = Usuario.objects.all()
    data = serializers.serialize("json", qs)
    return HttpResponse(data, content_type='application/json', status=200)


def torneos_json(request):
    qs = Torneo.objects.all()
    data = serializers.serialize("json", qs)
    return HttpResponse(data, content_type='application/json', status=200)


def partidos_json(request):
    qs = Partido.objects.all()
    data = serializers.serialize("json", qs)
    return HttpResponse(data, content_type='application/json', status=200)

def torneo_partidos_json(request, id):
    torneo_qs = Torneo.objects.filter(id = id)
    partidos_qs =  Partido.objects.filter(torneo = id)
    combined = list(chain(torneo_qs,partidos_qs))
    data = serializers.serialize("json",combined, use_natural_foreign_keys=True)

    return HttpResponse(data,content_type='application/json', status=200)

def id_usuario_x_username(request, username):
    usr = Usuario.objects.get(username = username)
    return HttpResponse(usr.id, content_type='application/json', status=200)


def login(request,username,password):
    usuario = Usuario.objects.get(username = username)
    _status = 400 
    if(usuario.password == password):         
         data = serializers.serialize('json', [ usuario, ])
         _status = 200
    else: 
        data = json.dumps("error")
     
    return  HttpResponse(data,content_type='application/json', status = _status)

#TODO USAR LAS LISTVIEWS EN LUGAR DE ESTO....

@csrf_exempt
def inscribir_jugador_partido(request):
    
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    jugador_id = body_data.get('id_jugador')
    partido_id = body_data.get('id_partido')

    print('jugador:', jugador_id ,' partido:', partido_id)
    resultado = Resultado.objects.create(puntos = -1)
    jugador = Usuario.objects.get(pk=jugador_id)
    print(jugador)
    resultado.jugadores.set([ jugador])
    resultado.partido = Partido.objects.get(pk=partido_id)
    print(resultado)
    resultado.save()
    
    return HttpResponse(status=200)

@csrf_exempt
def act_categoria(request):

    #Actualiza la categoria de un jugador
    
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    jugador_id = body_data.get('id_jugador')
    nueva_categoria = body_data.get('nueva_categoria')
    jugador = Usuario.objects.get(pk=jugador_id)
    
    print('jugador:', jugador_id ,' nueva_categoria:', nueva_categoria)
    jugador.categoria = nueva_categoria
    print(jugador)

    jugador.save()

    data = json.dumps(nueva_categoria)
    return HttpResponse(data,content_type='application/json', status=200)

def resultados_usuario(request, id):
    resultado_qs = Resultado.objects.filter(jugadores = id)
    data = serializers.serialize("json", resultado_qs)

    return HttpResponse(data,content_type='application/json', status=200)

def partidos_id(request, id):
    resultado_qs = Partido.objects.filter(id = id)
    data = serializers.serialize("json", resultado_qs)

    return HttpResponse(data,content_type='application/json', status=200)

def torneos_organiza_usuario(request, id):
    _organizador = Usuario.objects.get(id = id)
    torneos_qs = Torneo.objects.filter(organizador = _organizador)
    data =  serializers.serialize("json", torneos_qs)

    return HttpResponse(data,content_type='application/json', status=200)


def bienvenido(request):
    return HttpResponse('<h1> Bienvenido a padel app </h1>')


        