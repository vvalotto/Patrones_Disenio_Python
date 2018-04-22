from abc import ABCMeta, abstractmethod
from ..factura.factura import *

class Ruteador(metaclass=ABCMeta):

    @abstractmethod
    def rutear(self, factura):
        pass

