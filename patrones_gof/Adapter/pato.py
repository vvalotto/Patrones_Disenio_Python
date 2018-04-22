"""
Patron Adapter

Interfaz del adaptador
"""

from abc import ABCMeta, abstractmethod

class BasePato(metaclass=ABCMeta):
    '''
    Definición de la interfaz que define los tipos que usará el cliente.
    En este caso define el uso de los tipos de patos
    '''

    @abstractmethod
    def graznar(self):
        pass

    @abstractmethod
    def volar(self):
        pass

'''
Implementación tipos concretos de patos
'''
class PatoCriollo(BasePato):

    def graznar(self):
        print('Cuac!')

    def volar(self):
        print('Estoy volando!')
