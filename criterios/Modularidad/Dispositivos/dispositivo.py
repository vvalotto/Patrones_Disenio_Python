'''
Created on 09/11/2013

@author: voval
'''

from abc import ABCMeta, abstractmethod

class iCalculadorDescuento(metaclass=ABCMeta):
    '''
    classdocs
    '''

    @abstractmethod
    def obtener_descuento(self):
        pass
    

class Dispositivo(iCalculadorDescuento):

    def __init__(self,precio):
      self._lista_funcion = []
      self.precio = precio
      
    def crear_funcion(self, funcion):
        self._lista_funcion.append(funcion)
    
    def obtener_descuento(self):
        if (len(self._lista_funcion) > 5) :
            return 0.1
        else:
            return 0.05
    
            