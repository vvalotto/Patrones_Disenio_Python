
class Factura(object):

    def __init__(self, cantidad):
        self.cantidad = cantidad
        return

    def obtener_cantidad_cargada(self):
        return self.cantidad
