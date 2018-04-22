"""
Entidad Reclamo
"""

from .entidad import *


class Reclamo(Entidad):

    @property
    def cliente(self):
        return self._cliente

    @property
    def suministro(self):
        return self._suministro

    @property
    def exposicion_cliente(self):
        return self._exposicion_cliente

    def __init__(self):
        super().__init__()
        self._cliente = None
        self._suministro = None
        self._exposicion_cliente = None
        return


