'''
Created on 25/07/2013

@author: voval
'''
import math

class Termometro:
    def __init__(self):
        self._paso = 0
        self._cambio = 1
    
    def leer_temp(self):
        self._temp = (math.sin(self._paso) * 20) + 20
        self._paso = self._paso + (0.1 * self._cambio)
        return self._temp
    
    def cambiar_temp(self, cambio):
        if cambio:
            self._cambio = 1
        else:
            self._cambio = -1 
        