'''
Created on 03/01/2014

@author: vvalotto
'''

from factura import *
from calculador_deduccion import *
from calculador_iva import *

class CalculadorFactura():
    '''
    classdocs
    '''

    def __init__(self, factura, deduccion, iva):
        '''
        Constructor
        '''
        self._factura = factura
        self._calculador_deduccion = deduccion
        self._calculador_iva = iva
    
    def calcular_factura(self):
        self._calculador_deduccion.calcular(self._factura)
        self._calculador_iva.calcular (self._factura)
        self._factura.importe_total = self._factura.importe_factura - self._factura.importe_iva + self._factura.importe_deduccion
    