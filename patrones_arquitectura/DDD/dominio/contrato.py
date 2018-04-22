"""
Entidad Contrato
"""
from .entidad import *


class Contrato(BaseEntidad):

    @property
    def NIS(self):
        return self._NIS

    @property
    def tarifa(self):
        return self._tarifa

    @property
    def uso(self):
        return self._uso

    @property
    def ubicacion(self):
        return self._ubicacion

    @property
    def localidad(self):
        return self._localidad

    def __init__(self):
        super().__init__()
        return
