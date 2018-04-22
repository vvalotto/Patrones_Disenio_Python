'''
Created on 25/07/2013

@author: voval
'''

from dispositivo import *

class Motor(AbsDispositivo):
        
    def prende(self):
        self._activo = True
        print('Motor Prendido')
        return
        
    def apaga(self):
        self._activo = False
        print('Motor Apagado')
        return