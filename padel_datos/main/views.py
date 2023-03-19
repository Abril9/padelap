from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from itertools import chain
from rest_framework import viewsets


from .models import Torneo, Usuario, Partido
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

#TODO USAR LAS LISTVIEWS EN LUGAR DE ESTO....


def bienvenido(request):
    return HttpResponse('<h1> Bienvenido a padel app </h1>')


        