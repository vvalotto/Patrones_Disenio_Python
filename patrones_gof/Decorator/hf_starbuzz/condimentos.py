"""
Condimentos concretos que decoran los componentes
principales
"""

from .ibebida import *


class Mocha(CondimentoDecorador):

    def __init__(self, bebida):
        self._bebida = bebida
        return

    def pedir_descripcion(self):
        return self._bebida.pedir_descripcion() + \
            ", Mocha"

    def costear(self):
        return 0.20 + self._bebida.costear()


class Cortado(CondimentoDecorador):

    def __init__(self, bebida):
        self._bebida = bebida
        return

    def pedir_descripcion(self):
        return self._bebida.pedir_descripcion() + \
            ", Cortado"

    def costear(self):
        return 0.10 + self._bebida.costear()


class Soy(CondimentoDecorador):

    def __init__(self, bebida):
        self._bebida = bebida
        return

    def pedir_descripcion(self):
        return self._bebida.pedir_descripcion() + \
            ", Soy"

    def costear(self):
        return 0.15 + self._bebida.costear()


class Whip(CondimentoDecorador):

    def __init__(self, bebida):
        self._bebida = bebida
        return

    def pedir_descripcion(self):
        return self._bebida.pedir_descripcion() + \
            ", Whip"

    def costear(self):
        return 0.15 + self._bebida.costear()


