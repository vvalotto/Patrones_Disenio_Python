"""
Definiciones de OV de uso comun
"""
from .objeto_valor import *

class LetrasParaNombres:

    @staticmethod
    def letras():
        return ['a', 'b', 'c', 'd',
                'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n',
                'ñ', 'o', 'p', 'q', 'r',
                's', 't', 'v', 'u', 'v',
                'w', 'x', 'y', 'z']


class Nombre(ObjetoValor):

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    def __init__(self, nombre, apellido):

        if type(nombre) is not str:
            raise ErrorDeNombreVacio()

        if nombre == "":
            raise ErrorDeNombreVacio()

        if type(apellido) is not str:
            raise ErrorDeApellidoVacio()

        if apellido == "":
            raise ErrorDeApellidoVacio()

        for letra in nombre:
            if letra not in LetrasParaNombres.letras():
                raise ErrorDeNombreConSimbolos()

        for letra in apellido:
            if letra not in LetrasParaNombres.letras():
                raise ErrorDeNombreConSimbolos()

        self._nombre = nombre.capitalize()
        self._apellido = apellido.capitalize()
        return

    def mostrar_apellido_y_nombre(self):
        return self._apellido + ', ' + self._nombre

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._apellido, self._nombre]

    def __repr__(self):
        return self._nombre + " " + self._apellido

    def __str__(self):
        return self._nombre + " " + self._apellido


class ErrorDeNombreVacio(Exception):
    pass


class ErrorDeApellidoVacio(Exception):
    pass


class ErrorDeNombreConSimbolos(Exception):
    pass


class ErrorDeApellidoConSimbolos(Exception):
    pass


class Genero(ObjetoValor):

    def __init__(self, genero):

        if type(genero) is not str:
            raise ErrorDeGeneroVacio()

        if genero == "":
            raise ErrorDeGeneroVacio()

        self._genero = genero

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._genero]


class ErrorDeGeneroVacio(Exception):
    pass
