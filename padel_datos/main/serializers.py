from .models import Usuario, Torneo, Partido
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
                  'puntos'
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
