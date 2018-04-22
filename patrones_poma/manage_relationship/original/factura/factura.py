
class Factura(object):

    def __init__(self, calculador, cantidad):
        self.calculador = calculador
        self.cantidad = cantidad
        return

    def obtener_cantidad_cargada(self):
        return self.cantidad

    def pagar(self):
        descuento = 1 - self.calculador.obtener_descuento()
        a_pagar = self.cantidad * descuento
        return a_pagar