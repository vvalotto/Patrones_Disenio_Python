'''
Created on 03/01/2014

@author: vvalotto

'''
from datetime import *

class Factura:
    '''
    Clase que representa al entidad Factura y es un modelo de dicha entidad
    Solo contiene la definicion de sus atributos.
    '''


    def __init__(self):
        '''
        Inicializa el contenido de los atributos de la entidad con valores por defecto
        '''
        self._codigo = "Sin Codigo"
        self._fecha_emision = datetime.now()
        self._importe_factura = 0
        self._importe_iva = 0
        self._importe_deduccion = 0
        self._importe_total = 0
        self._porcentaje_deduccion = 0
        
    def _get_codigo (self):
        return self._codigo
    
    def _set_codigo (self, valor):
        self._codigo = valor
        
    def _get_fecha_emision (self):
        return self._fecha_emision
    
    def _set_fecha_emision (self, valor):
        self._fecha_emision = valor
        
    def _get_importe_factura (self):
        return self._importe_factura
    
    def _set_importe_factura (self, valor):
        self._importe_factura = valor
        
    def _get_importe_iva (self):
        return self._importe_iva
    
    def _set_importe_iva (self, valor):
        self._importe_iva = valor
    
    def _get_importe_deduccion (self):
        return self._importe_deduccion
    
    def _set_importe_deduccion (self, valor):
        self._importe_deduccion = valor

    def _get_importe_total (self):
        return self._importe_total
    
    def _set_importe_total (self, valor):
        self._importe_total = valor
   
    def _get_porcentaje_deduccion (self):
        return self._porcentaje_deduccion
    
    def _set_porcentaje_deduccion (self, valor):
        self._porcentaje_deduccion = valor

    codigo = property(_get_codigo, _set_codigo)
    fecha_emision = property(_get_codigo, _set_codigo)
    importe_factura = property(_get_importe_factura, _set_importe_factura)
    importe_iva = property(_get_importe_iva, _set_importe_iva)
    importe_deduccion = property(_get_importe_deduccion, _set_importe_deduccion)
    importe_total = property(_get_importe_total, _set_importe_total)
    porcentaje_deduccion = property (_get_porcentaje_deduccion, _set_porcentaje_deduccion)

