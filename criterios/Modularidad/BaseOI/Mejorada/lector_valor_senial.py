'''
Created on 25/11/2013

@author: voval
'''
from abc import ABCMeta, abstractmethod


class aLectorValorSenial(metaclass=ABCMeta):

    @abstractmethod
    def leer_dato(self):
        pass


class LectorSimple(aLectorValorSenial):
    
    def LectorSimple(self):
        pass
    
    def leer_dato(self):
        dato = input('Valor:')
        while not(dato.isnumeric()):
            print('Dato mal ingresado, <enter>')
            dato = input('Valor:')
        return dato
    
class LectorPrueba(aLectorValorSenial):
    import random
    
    def LectorPrueba(self):
        pass
    
    def leer_dato(self):
        dato = self.random.randint(0,50)
        return dato