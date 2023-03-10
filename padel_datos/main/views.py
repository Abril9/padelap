from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import Torneo, Usuario

def usuarios_json(request):
    qs = Usuario.objects.all()
    data = serializers.serialize("json", qs)
    return HttpResponse(data, content_type='application/json', status=200)


def crear_usuario(self, request):
    print('llego al post')
    
    data = json.loads(request.body)

    print(request.method)
    print(data)
    return HttpResponse('concha', content_type='application/json', status=200)

def torneo(request):
    lista_torneos = Torneo.objects.all()
    
    #return(mismorequest, path al html considerando que une todas las carpetas templates en una, contexto expresado como un dic de py)
    return render(request,"main/torneo.html", {
        "lista_torneos": lista_torneos
    })










def bienvenido(request):
    return HttpResponse('<h1> Bienvenido a padel app </h1>')

def crear_usuario(request):
    
    data = request.data
    usuario = Usuario.objects.create( nombre =  data.nombre, apellido = 'apellido?', email = data.email,
                                                wsp = data.wsp, username = data.username, password = data.password)
    usuario.save()

def obtener_usuario(username):
    usuario = Usuario.objects.filter(username = username)
    return usuario