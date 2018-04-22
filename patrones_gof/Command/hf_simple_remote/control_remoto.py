"""

"""

from .command import *


class ControlRomotoSimple(object):

    @property
    def slot(self):
        return self._slot

    @slot.setter
    def slot(self, valor):
        self._slot = valor
        return

    def __init__(self):
        self._slot = None
        return

    def presionar_boton(self):
        self._slot.ejecutar()
        return
