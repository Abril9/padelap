import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from itertools import chain
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt


from .models import Jugador, Resultado, Torneo, Usuario, Partido
from .serializers import UsuarioSerializer, PartidoSerializer, TorneoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer

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
    #params = request.params 
    
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    jugador_id = body_data.get('id_jugador')
    partido_id = body_data.get('id_partido')

    resultado = Resultado.objects.create(puntos = -1)
    resultado.jugadores.set([Jugador.objects.get(pk=jugador_id)])
    resultado.partido = Partido.objects.get(pk=partido_id)
    print(resultado)
    resultado.save()
    
    return HttpResponse(status=200)



def bienvenido(request):
    return HttpResponse('<h1> Bienvenido a padel app </h1>')


        