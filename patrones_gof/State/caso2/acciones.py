from abc import ABCMeta, abstractmethod


class Accion(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def ejecutar(self):
        pass


class AccionPrender(Accion):

    def ejecutar(self):
        print('Indicador de Power Prendida')
        return


class AccionApagar(Accion):

    def ejecutar(self):
        print('Indicador de Power Apagado')
        return


class AccionError(Accion):

     def ejecutar(self, mensaje):
         print(mensaje)
