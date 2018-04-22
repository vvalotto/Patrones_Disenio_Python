from abc import ABCMeta, abstractmethod

class CalculadorDescuento(metaclass=ABCMeta):

    @abstractmethod
    def obtener_descuento(self):
        pass

    def __init__(self):
        pass