'''
Created on 04/01/2014

@author: vvalotto


'''
from abc import ABCMeta, abstractmethod

class ACalculadorIVA(object):
    '''
    Clase Abstracta que especifica el calculador de IVA
    '''
        
    @abstractmethod
    def calcular(self, factura):       
        pass
    

class CalculadorIVA(ACalculadorIVA):
    '''
    Implementacion del cálculo del IVA de manera simple
    '''
    
    def __init__(self):
        
        self._IVA = [0.21]
    
    def calcular(self, factura):
        factura._importe_iva = factura._importe_factura * self._IVA
    

    