'''
Created on 04/01/2014

@author: vvalotto


'''
from abc import ABCMeta, abstractmethod

class ACalculadorDeduccion(object):
    '''
    Clase Abstracta que especifica el calculador de deducciones
    '''
        
    @abstractmethod
    def calcular(self, factura):       
        pass


class CalculadorDeduccion(ACalculadorDeduccion):
    '''
    Calculador de deduccion simple
    '''
    def calcular(self, factura):
        '''
        Realiza el calculo de la deduccion.
        En la factura viene el porcentaje de deduccion asignado desde una
        clase cliente.
        En este caso el calculo es simplemente la aplicacion del porcentaje
        '''    
        factura.importe_deduccion = factura.importe_factura * factura.porcentaje_deduccion /100
       

class CalculadorDeduccionProp(ACalculadorDeduccion):
    
    def __init__(self):
        self._tabla_porcentaje = [[100,5],[200,10],[500,15],[1000,20]]
    
    def calcular(self, factura):
        '''
        Realiza el calculo de la deduccion.
        En funcion de importe de la factura se hace una deduccion segun la tabla de
        deducciones
        '''
        for iterador in self._tabla_porcentaje:
            print(t)
            if (t > factura.importe_factura):
                factura.porcentaje_deduccion = iterador[1]
                factura.importe_deduccion = factura.importe_factura * factura.porcentaje_deduccion /100
                return
            
        factura.porcentaje_deduccion = iterador[1]
        factura.importe_deduccion = factura.importe_factura * factura.porcentaje_deduccion /100
        return
    
        
    