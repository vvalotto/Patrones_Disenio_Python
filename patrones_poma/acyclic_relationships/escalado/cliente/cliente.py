
from ..factura.factura import *

class Cliente(object):

    def __init__(self):
        self.facturas = []
        return

    def obtener_descuento(self):
        if len(self.facturas) > 5:
            return 0.1
        else:
            return 0.03

    def obtener_facturas(self):
        return self.facturas

    def crear_factura(self, cantidad):
        factura = Factura(cantidad)
        self.facturas.append(factura)
        return
