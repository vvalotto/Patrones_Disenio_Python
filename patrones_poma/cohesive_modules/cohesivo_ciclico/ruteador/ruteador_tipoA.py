from .ruteador import *
from ..factura.factura import *

class RuteadorTipoA(Ruteador):

    def rutear(self, factura):
        return "UBICACION_A"