"""
Componentes concretos para decorar
"""

from .ibebida import *


class Expresso(Bebida):

    def __init__(self):
        self._descripcion = "Expresso"
        return

    def costear(self):
        return 1.99


class HouseBlend(Bebida):

    def __init__(self):
        self._descripcion = "House Blend Coffe"
        return

    def costear(self):
        return 0.99


class Decaf(Bebida):

    def __init__(self):
        self._descripcion = "Decaf"
        return

    def costear(self):
        return 1.05


class DarkRoast(Bebida):

    def __init__(self):
        self._descripcion = "Dark Roast"
        return

    def costear(self):
        return 0.99
