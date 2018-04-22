"""
Ejemplo de manejo de estado con una resolución con el Patron State
"""

from abc import ABCMeta, abstractmethod
from acciones import *


class EstadoBase(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def prender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def aumentar(self):
        pass

    @abstractmethod
    def disminuir(self):
        pass


class EstadoPrendido(EstadoBase):

    def __init__(self, disp):
        self._disp = disp
        return

    def iniciar(self):
        print('El dispositivo ha comenzado a trabajar')
        self._disp.pasar_a_estado(self._disp.estado_trabajando)
        return

    def prender(self):
        AccionError().ejecutar('El disp ya está prendido')
        return

    def apagar(self):
        AccionApagar().ejecutar()
        self._disp.pasar_a_estado(self._disp.estado_apagado)
        return

    def aumentar(self):
        print('El dispositivo ha comenzado a trabajar')
        self._disp.pasar_a_estado(self._disp.estado_trabajando)
        return

    def disminuir(self):
        print('El dispositivo no esta trabajando')
        return


class EstadoApagado(EstadoBase):

    def __init__(self, disp):
        self._disp = disp

    def iniciar(self):
        print('El dispositivo tiene que prenderse primero')
        pass

    def prender(self):
        AccionPrender().ejecutar()
        self._disp.pasar_a_estado(self._disp.estado_prendido)
        pass

    def apagar(self):
        AccionError().ejecutar('El dispositivo ya esta apagado')
        pass

    def aumentar(self):
        print('El dispositivo no esta trabajando')
        return

    def disminuir(self):
        print('El dispositivo no esta trabajando')
        return


class EstadoTrabajando(EstadoBase):

    def __init__(self, disp):
        self._disp = disp

    def iniciar(self):
        print('El dispositivo ya está trabajando')
        pass

    def prender(self):
        print('El dispositivo ya está trabajando')
        pass

    def apagar(self):
        print('El dispositivo se ha apagado')
        self._disp.pasar_a_estado(self._disp.estado_apagado)
        pass

    def aumentar(self):
        print('Aumento')
        return

    def disminuir(self):
        print('Disminuyo')
        return


class Dispositivo(object):

    @property
    def estado_apagado(self):
        return self._estado_apagado

    @property
    def estado_prendido(self):
        return self._estado_prendido

    @property
    def estado_trabajando(self):
        return self._estado_trabajando

    @property
    def variable(self):
        return self._variable

    def __init__(self):
        self._estado_apagado = EstadoApagado(self)
        self._estado_prendido = EstadoPrendido(self)
        self._estado_trabajando = EstadoTrabajando(self)
        self._estado = self._estado_apagado
        self._paso = 10
        self._variable = 0
        self._tope = 50
        return

    def prender(self):
        self._estado.prender()
        return

    def apagar(self):
        self._variable = 0
        self._estado.apagar()
        return

    def iniciar(self):
        self._variable += self._paso
        self._estado.iniciar()
        return

    def aumentar(self):
        if (self._variable + self._paso) > self._tope:
            print('No se puede aumentar mas')
        else:
            self._variable += self._paso
            self._estado.aumentar()
        return

    def disminuir(self):

        if self._variable <= 0:
            self._estado.apagar()
        else:
            self._variable -= self._paso
            self._estado.disminuir()
        return

    def pasar_a_estado(self, estado):
        self._estado = estado


if __name__ == '__main__':
    dispositivo = Dispositivo()
    dispositivo.prender()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.iniciar()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.aumentar()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.aumentar()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.aumentar()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.aumentar()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.aumentar()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.disminuir()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.prender()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.disminuir()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.disminuir()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.disminuir()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.disminuir()
    print('Valor:' + str(dispositivo.variable))
    dispositivo.disminuir()
    print('Valor:' + str(dispositivo.variable))
