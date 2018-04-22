from abc import ABCMeta, abstractmethod

class Ruteador(metaclass=ABCMeta):

    @abstractmethod
    def rutear(self, Factura):
        pass

