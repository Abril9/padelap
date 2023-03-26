from .models import Usuario, Torneo, Partido, Jugador
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido',
            'email',
            'wsp',
            'username',
            'password',
            'categoria',
            'genero',
            'edad',
        ]


class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = [
            'nombre',
            'apellido',
            'email',
            'wsp',
            'username',
            'password',
            'categoria',
            'genero',
            'edad',
        ]


class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = [
            'nombre',
            'inicio_inscripcion',
            'fin_inscripcion',
            'inicio',
            'fin',
            'organizador',
            'ciudad',
            'cupo_maximo_inscripcion',
            'puntos',
            'categorias'
        ]


class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = [
            'torneo',
            'fecha',
            'cede',
            'genero',
            'puntos_ganadores',
            'puntos_perdedores',
        ]
