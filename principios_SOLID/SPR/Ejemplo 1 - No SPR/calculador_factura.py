'''
Created on 03/01/2014

@author: vvalotto

Ejemplo de la violacion a Principio de Resposanbilidad Unica

'''

from factura import Factura

class CalculadorFactura():
    '''
    Clase Responsable de Calculo del importe de la factura
    '''


    def __init__(self, factura):
        '''
        El constructor del calculador recibe la factura que debera calcular
        '''
        self._factura = factura
    
    def calcular_factura(self):
        '''
        Para este caso en este metodo se realiza el calculo de:
        - la deduccion en funcion del porcentaje 
        - el iva
        - Importe total teniendo en cuenta los anteriores calculos
        Cualquier cambio en la manera de calcular la deduccion, el iva o el importe
        afecta todos las clases que usan este calculador.
        El calculador de factura solo deberia saber cuales son los items 
        que integra un factura y como interviene en el importe final, pero no saber
        como se calcula cada uno, ya que cada uno de estos calculos puede cambiar
        segun decisiones no conocidas por el calculador de factura
        '''
        
        self._factura.importe_deduccion = (self._factura.importe_factura * self._factura.porcentaje_deduccion) / 100
        self._factura.importe_iva = self._factura.importe_factura * 0.21
        self._factura.importe_total = self._factura.importe_factura - self._factura.importe_iva + self._factura.importe_deduccion
    