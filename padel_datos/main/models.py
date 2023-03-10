from django.db import models

from .utils import Categoria, Genero

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    apellido = models.CharField(max_length=250, null=False)
    email = models.EmailField(max_length=250, null=False)
    wsp = models.CharField(max_length=250, null=False)
    username = models.CharField(max_length=250, null=False)
    password = models.CharField(max_length=250, null=False)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    """
         Devuelve la url para acceder a una instancia particular de MyModelName.
    """

    def get_absolute_url(self):
        return f'{self.id}/usuario'

    def __str__(self):
        return 'Usuario %s - %s' % (self.username, self.email)
    # def _crear_(data, self):
    #         self.nombre : data.nombre
    #         self.apellido : data.apellido
    #         self.email : data.email
    #         self.wsp : data.wsp
    #         self.username : data.username
    #         self.password : data.password
    #         return self




class Jugador(models.Model):
    #cambiar
    usr = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    #categoria = models.TextChoices(Categoria),
    #avatar = models.ImageField(upload_to='/files_source')
    # genero = models.TextChoices(Genero)
    edad = models.IntegerField()
    #todo ciudades como enum o api o algo
    passwordcudad = models.CharField(max_length=250, null = False)
    
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
'''
class Torneo(models.Model):
    nombre = models.CharField(max_length=200)
    inicio_inscripcion = models.DateField()
    fin_inscripcion = models.DateField()
    inicio = models.DateField()
    fin = models.DateField()
    categorias = models.IntegerField(choices=Categoria.choices(), default=Categoria.NO_CATEGORIZAD)
    cedes = models.CharField(max_length=200) 
    #TODO modelar cedes de otra forma

    def get_categoria(self):
        return Categoria(self.type).name.title()

class Resultado(models.Model):
     jugadores = models.ManyToManyField(Jugador, max_length=2)
     puntos = models.IntegerField()

'''
los Partidos masculinos son en realidad torneos libres, puede anotarse cualquiera
'''
class Partido(models.Model):
     torneo = models.ForeignKey(Torneo, on_delete=models.PROTECT)
     fecha = models.DateTimeField()
     cede = models.CharField(max_length=200)
     genero = models.IntegerField(choices=Genero.choices())
     resultado = models.ManyToManyField(Resultado, max_length=2)
     #????googlear
     puntos = models.IntegerField()