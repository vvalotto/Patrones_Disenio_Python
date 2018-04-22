from ..factura.calculador_descuento import *
from ..factura.factura import *

class Cliente(CalculadorDescuento):

    def __init__(self):
        self.facturas = []
        return

    def obtener_descuento(self):
        if len(self.facturas) > 5:
            return 0.1
        else:
            return 0.03

    def obtener_Facturas(self):
        return self.facturas

    def crear_factura(self, cls, cantidad):
        factura = Factura(cls, cantidad)
        self.facturas.append(factura)
        return