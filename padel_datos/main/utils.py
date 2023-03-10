from enum import IntEnum


'''
La categoria más alta es la primera.

'''


# class Categoria(models.TextChoices):
#     PRIMERA = '1# Primera'
#     SEGUNDA = '2# Segunda'
#     TERCERA = '3# Tercera'
#     CUARTA = '4# Cuarta'
#     QUINTA = '5# Quinta'
#     SEXTA = '6# Sexta'
#     SEPTIMA = '7# Septima'
#     PRINCIPIANTE = 'Principiante'
#     NO_CATEGORIZAD = 'NC No categorizad'

#     categoria = models.CharField(
#         max_length=2,
#         choices=self.Categoria.choices,
#         default=Categoria.NO_CATEGORIZAD,
#     )

#     def get_categoria(self) -> categoria:
#         # Get value from choices enum
#         return self.Categoria[self.categoria]
    
# class Genero(models.TextChoices):
#         FEMENINO = 'Femenino'
#         MASCULINO = 'Másculino'
#         NO_BINARI0 = 'No binario'
#         OTRO = 'Otro'

# genero = models.CharField(
#         max_length=2,
#         choices=Genero.choices,
#         default=Genero.OTRO,
#     )

# def get_genero(self) -> genero:
#         # Get value from choices enum
#         return self.Genero[self.genero]

class Categoria(IntEnum):
    PRIMERA =1
    SEGUNDA =2
    TERCERA =3
    CUARTA = 4
    QUINTA = 5
    SEXTA = 6
    SEPTIMA =7 
    PRINCIPIANTE = 8
    NO_CATEGORIZAD = 9

    @classmethod
    def choices(cls):
        return  [(key.value, key.name) for key in cls]
    
class Genero(IntEnum):
    FEMENINO = 1
    MASCULINO = 2
    NO_BINARI0 = 3
    OTRO = 4

    @classmethod
    def choices(cls):
        return  [(key.value, key.name) for key in cls]