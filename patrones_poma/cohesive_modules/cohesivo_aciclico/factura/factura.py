from ..ruteador.Ruteable import *

class Factura(Ruteable):

    ALTA = "01"
    BAJA = "02"

    @property
    def tipo(self):
        return self._tipo

    @property
    def ubicacion(self):
        return self._ubicacion

    @property
    def cantidad(self):
        return self._cantidad

    def __init__(self, tipo, ubicacion, cantidad, ruteador):
        self._tipo = tipo;
        self._ubicacion = ubicacion
        self._cantidad = cantidad
        self._ruteador = ruteador

    def obtener_prioridad(self):
        if self._cantidad < 1000.00:
            return Factura.BAJA
        else:
            return Factura.ALTA

    def rutear(self):
        return self._ruteador.rutear(self)
