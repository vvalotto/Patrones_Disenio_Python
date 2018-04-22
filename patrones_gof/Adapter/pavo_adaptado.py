"""
Patron Adapter:

Adaptador: Implementa la interfaz del tipo a adaptar
y compone el tipo que se usara finalmente

El Pavo se usa como si fuera un pato
"""

from .pato import *


class PavoAdaptado(BasePato):

    def __init__(self, pavo):
        self._pavo = pavo

    def graznar(self):
        self._pavo.guglutear()

    def volar(self):
        for i in range(0, 4):
            self._pavo.volar()
