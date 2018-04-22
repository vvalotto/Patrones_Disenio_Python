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