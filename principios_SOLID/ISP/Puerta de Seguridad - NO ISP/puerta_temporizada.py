'''
Created on 27/07/2013

@author: voval
'''

from puerta import *
import time

class PuertaTemporizada(AbsPuerta):
    
    def __init__(self):
        self._estado = True
    
    def bloquear(self):
        if self._estado:
            print('Ya esta bloqueada')
        else:
            self._estado = True
            print('Se Cerro la puerta')
        return
    
    def desbloquear(self):
        if not self._estado:
            print('Ya esta desbloqueda')
        else:
            self._estado = False
            print('Se Abrio la puerta')
        return
    
    def puerta_abierta(self):
        return  print('Cerrada') if self._estado else print('Abierta')
    
    def timeout(self):
        time.sleep(self.tiempo)    
        print('Riiiing - se va cerra la puerta')
        self.bloquear()
        return
    
    def _set_tiempo(self,value):
        self._tiempo = value
        return
    
    def _get_tiempo(self):
        return self._tiempo
    
    tiempo = property(_get_tiempo, _set_tiempo)

        
    