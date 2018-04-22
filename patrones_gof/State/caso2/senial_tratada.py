"""
Paquete Senial
Modulo Senial Tratada
"""

class SenialTratada(object):

    @property
    def senial_tratada(self):
        return self.__senial

    def __init__(self, senial, procesador):
        self.__senial = senial
        self.__procesador = procesador
        return

    def procesar(self):
        return