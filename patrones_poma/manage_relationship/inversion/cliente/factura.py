from abc import ABCMeta, abstractmethod

class Factura(metaclass=ABCMeta):

    @abstractmethod
    def obtener_cantidad_cargada(self):
        pass

    @abstractmethod
    def pagar(self):
        pass


