

class MediadorPago(object):

    def __init__(self, cliente):
        self._cliente = cliente

    def pagar(self, factura):
        descuento = 1 - self._cliente.obtener_descuento()
        a_pagar = factura.cantidad * descuento
        return a_pagar
