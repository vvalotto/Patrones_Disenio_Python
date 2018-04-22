'''
Created on 21/07/2013

@author: voval
'''
from abc import ABCMeta, abstractmethod

class AbsServidor:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def Saludar(self):
        pass

class ServidorA(AbsServidor):
    def Saludar(self, cliente):
        print ('Hola ' + cliente + ' , soy tu servidor')

class ServidorB(AbsServidor):
    def Saludar(self, cliente):
        print ('Hola estimadisimo' + cliente + ' , en que lo puedo ayudar')
