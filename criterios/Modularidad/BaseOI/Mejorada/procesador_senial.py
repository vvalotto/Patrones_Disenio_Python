'''
Created on 25/11/2013

@author: voval
'''

from abc import ABCMeta, abstractmethod

class aProcesadorSenial(metaclass=ABCMeta):

    @abstractmethod
    def procesar_señal(self):
        pass
    
class ProcesadorMax(aProcesadorSenial):
    
    def __init__(self):
        pass
    
    def procesar_señal(self, datos):
        return max(datos)
        