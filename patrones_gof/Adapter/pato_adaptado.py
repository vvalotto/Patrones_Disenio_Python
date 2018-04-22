"""
Patron Adapter:

Adaptador: Implementa la interfaz del tipo a adaptar
y compone el tipo que se usara finalmente

El Pato se usa como si fuera un pavo
"""

from .pavo import *

class PatoAdaptado(BasePavo):

    def __init__(self, pato):
        self._pato = pato

    def guglutear(self):
        self._pato.graznar()

    def volar(self):
        self._pato.volar()
        print('Pero no deberia hacerlo tanto')