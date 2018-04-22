"""
Entidad Cliente
"""
from .entidad import *


class Cliente(BaseEntidad):

    @property
    def documento(self):
        return self._documento

    @property
    def nombre(self):
        return self._nombre

    @property
    def domicilo_postal(self):
        return self._domicilio

    @property
    def telefono(self):
        return self._telefono

    def asignar_documento(self, documento):
        self._documento = documento
        return

    def asignar_nombre(self, nombre):
        self._nombre = nombre
        return

    def asignar_domicilio_postal(self, domicilio):
        self._domicilio = domicilio
        return

    def asignar_telefono_contacto(self, telefono):
        self._telefono = telefono
        return