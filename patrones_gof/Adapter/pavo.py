"""

"""

from abc import ABCMeta, abstractmethod

class BasePavo(metaclass=ABCMeta):
    '''
    Definición de la clase abstracta (tipo interfaz) para los tipos pavos
    '''

    @abstractmethod
    def guglutear(self):
        pass

    @abstractmethod
    def volar(self):
        pass

'''
Implementación tipos concretos de patos
'''
class PavoSilvestre(BasePavo):

    def guglutear(self):
        print('Glub Glub!')

    def volar(self):
        print('Vuelo poca distancia!')