'''
Created on 24/07/2013

@author: voval
'''
from lampara import *

class Boton:
    def __init__(self):
        self._estado = False
        self._l = Lampara()
        return
    
    def Presionar(self):
        
        if self._estado:
            self._l.apaga()
        else:
            self._l.prende()
            
        self._estado = not self._estado
        return
        