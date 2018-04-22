"""
Inicio Decorator Pattern
"""

from abc import abstractmethod

class Bebida(object):
    """
    Clase abstracta que encapsula lo esencial del tipo (elemento) sobre lo que se va a decorar
    """
    def __init__(self):
        self._descripcion = "Bebida desconocida"
        return

    def pedir_descripcion(self):
        return self._descripcion

    @abstractmethod
    def costear(self):
        pass


class CondimentoDecorador(Bebida):
    """
    Clase abstracta que define el comportamiento básico del tipo de decoración
    """
    @abstractmethod
    def pedir_descripcion(self):
        pass


