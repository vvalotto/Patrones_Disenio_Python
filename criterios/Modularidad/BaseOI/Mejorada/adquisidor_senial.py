'''
Created on 24/11/2013

@author: voval
'''
from senial import *
from lector_valor_senial import *

class AdquisidorSenial(object):
    '''
    classdocs
    '''

    def __init__(self,senial, lectorvalor):
        self._senial = senial
        self._lector_valor = lectorvalor
    
    def leer_senial(self):       
        while (self._senial.llenar(self._lector_valor.leer_dato())):
            pass
      
    def mostrar_señal(self):
        print(self._senial.obtener())