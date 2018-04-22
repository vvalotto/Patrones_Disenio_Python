"""
Paquete Senial
modulo Procesador
"""

from abc import ABCMeta, abstractmethod

class Procesador(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def obtener_parametro(self):
        pass
