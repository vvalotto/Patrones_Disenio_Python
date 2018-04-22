"""

"""

from abc import abstractmethod, ABCMeta


class AbsComando(metaclass=ABCMeta):

    @abstractmethod
    def ejecutar(self):
        pass


class ComandoPrenderLuz(AbsComando):

    def __init__(self, luz):
        self._luz = luz
        return

    def ejecutar(self):
        self._luz.prender()
        return


class ComandoApagarLuz(AbsComando):

    def __init__(self, luz):
        self._luz = luz
        return

    def ejecutar(self):
        self._luz.apagar()
        return


class ComandoAbrirGarage(AbsComando):

    def __init__(self, puerta_garage):
        self._puerta_garage = puerta_garage
        return

    def ejecutar(self):
        self._puerta_garage.abrir()
        return


