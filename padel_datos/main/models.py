from django.db import models 
from django_jsonfield_backport.models import JSONField

from .utils import Categoria, Genero

class Usuario(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    apellido = models.CharField(max_length=250, null=False)
    email = models.EmailField(max_length=250, null=False, unique = True)
    wsp = models.CharField(max_length=250, null=False)
    username = models.CharField(max_length=100, null=False, unique = True)
    
    categoria = models.IntegerField(default=-1)
    #avatar = models.ImageField(upload_to='/files_source', null=True)
    genero = models.IntegerField(null=True)
    edad = models.IntegerField(null = True)
    
    
    password = models.CharField(max_length=20, null=False)
    #TODO googlear como almacenar contraseñas con django, como las encripto en la bdd 
    #level3

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    #TODO googlear para que servia esto jaja level5
    def get_absolute_url(self):
        return f'{self.id}/usuario'

    def __str__(self):
        return 'Usuario %s - %s' % (self.username, self.password)

class Jugador(models.Model):
    #usr = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)


    nombre = models.CharField(max_length=250, null=False)
    apellido = models.CharField(max_length=250, null=False)
    email = models.EmailField(max_length=250, null=False, unique = True)
    wsp = models.CharField(max_length=250, null=False)
    username = models.CharField(max_length=100, null=False, unique = True)
    
    password = models.CharField(max_length=20, null=False)
    #TODO cambiar - level2.. aplicar bien estoy en eso
    categoria = models.IntegerField(choices=Categoria.choices(), null=True),
    #avatar = models.ImageField(upload_to='/files_source', null=True)
    genero = models.IntegerField(choices=Genero.choices(), null=True)
    edad = models.IntegerField()
    
    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
        
    def get_absolute_url(self):
        return f'{self.id}/jugador'
    
    def __str__(self):
        return 'Jugador %s' % (self.usr.username)
    

    
''' 
blank determines whether the field will be required in forms. This includes the admin and your custom forms. 
If blank=True then the field will not be required, whereas if it's False the field cannot be blank.


Los torneos tienen una ciudad de cede y un periodo durante el cual realizar una inscripcion, también
un cupo máximo de jugadores que pueden inscribirse, luego de cerrado el proceso de inscripcion se consiguen
y publican las cedes del sorteo. El organizamodor decide cuantos puntos se entregan para el ganador
y para el eprdedor de cada partido.

'''
class Torneo(models.Model):
    nombre = models.CharField(max_length=200, unique = True)
    inicio_inscripcion = models.DateField()
    fin_inscripcion = models.DateField()
    inicio = models.DateField()
    fin = models.DateField()
    organizador = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    ciudad = models.CharField(max_length=200) 
    cupo_maximo_inscripcion = models.IntegerField(null=True)
    puntos = models.IntegerField()
    categorias = JSONField(default={ 'cat' : [-1]})



'''
los Partidos masculinos son en realidad torneos libres, puede anotarse cualquiera

El organizamodor decide cuantos puntos se entregan para el ganador y para el perdedor de cada partido, 
de acuerdo a la instancia del torneo.

Los puntos quedan sumados al jugador para esa categoria - TODO level3
'''
class Partido(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, null=True)
    fecha = models.DateTimeField()
    cede = models.CharField(max_length=200)
    #TODO modelar cedes de otra forma - level4
    genero = models.IntegerField(choices=Genero.choices())
    
    #el organizador decide cuantos puntos se entregan por instancia para el ganadr y para el perdedor
    puntos_ganadores = models.IntegerField()
    puntos_perdedores = models.IntegerField()


class Resultado(models.Model):
    jugadores = models.ManyToManyField(Usuario, max_length=2)
    puntos = models.IntegerField(null = True)
    partido = models.ForeignKey(Partido, on_delete=models.PROTECT, max_length=2, null= True)
    #TODO cargar resultado - level 2
