from vuelo import *
from graznido import *

from abc import  ABCMeta, abstractmethod


class Pato(metaclass=ABCMeta):

    def __init__(self):
        self.vuelo = None
        self.graznido = None

    @abstractmethod
    def visualizar(self):
        pass

    def hacer_graznido(self):
        self.graznido.graznar()

    def realizar_vuelo(self):
        self.vuelo.volar()

    def nadar(self):
        print ('Todos los patos nadan')


class PatoReal(Pato):

    def __init__(self):
        self.vuelo = VueloConAlas()
        self.graznido = GraznidoFuerte()

    def visualizar(self):
        print('Yos un pato real')


class PatoModelado(Pato):

    def __init__(self):
        self.vuelo = SinVuelo()
        self.graznido = GraznidoFuerte()

    def visualizar(self):
        print('Yos un pato modelado')
