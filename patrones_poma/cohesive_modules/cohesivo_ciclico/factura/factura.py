from ..ruteador.ruteador_tipoA import *

class Factura(object):

    @property
    def tipo(self):
        return self._tipo

    @property
    def ubicacion(self):
        return self._ubicacion

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def ruteador(self):
        return self._ruteador.rutear(self)

    def __init__(self, tipo, ubicacion, cantidad, ruteador):
        self._tipo = tipo;
        self._ubicacion = ubicacion
        self._cantidad = cantidad
        self._ruteador = ruteador
