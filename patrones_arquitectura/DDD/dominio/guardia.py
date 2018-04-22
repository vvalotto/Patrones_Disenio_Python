"""
Entidad Guardia
"""

from .entidad import *


class Guardia(BaseEntidad):

    @property
    def nombre(self):
        return self._nombre

    @property
    def area(self):
        return self._area

    def __init__(self):
        super().__init__()
        self._nombre = None
        self._area = None
        return

