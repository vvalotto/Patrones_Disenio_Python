"""
Entidad Incidencia
"""

from .entidad import *


class Incidencia(BaseEntidad):

    OK = True
    @property
    def area(self):
        return self._area

    @property
    def alimentador(self):
        return self._alimentador

    @property
    def trafo(self):
        return self._trafo

    @property
    def probable_de_falla(self):
        return self._probable_de_falla

    def __init__(self):
        super().__init__()
        self._alimentador = None
        self._trafo = None
        self._probable_de_falla = None
        return

    def asignar_alimentador(self, alimentador):

        if self._validar_alimentador(alimentador) is not self.OK:
            raise Exception()
        self._alimentador = alimentador
        return

    def asignar_probable_de_falla(self, probable_de_falla):

        if self._validar_probable_de_falla(probable_de_falla) is not self.OK:
            raise Exception()
        self._probable_de_falla = probable_de_falla
        return

