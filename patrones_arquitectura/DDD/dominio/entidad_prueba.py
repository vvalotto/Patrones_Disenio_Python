"""
Entidad de Prueba
"""

from .entidad import *


class Prueba(BaseEntidad):

    @property
    def atributo(self):
        return self._atributo

    def __init__(self):
        super().__init__()
        self._atributo = None
        return

    def asignar_atributo(self, atributo):
        self._atributo = atributo
        return


