'''
Created on 09/11/2013

@author: voval
'''

from servicio import ServicioImp

class Cliente(object):
    '''
    classdocs
    '''


    def __init__(self, dato):
        self._dato = dato
        
    def usar_servicio(self, servicio):
        servicio.hacer()
        
    