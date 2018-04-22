'''
Created on 25/07/2013

@author: voval
'''
from dispositivo import *

class Lampara(AbsDispositivo):
    def prende(self):
        self._activo = True
        print('Luz Pendida')
        return
        
    def apaga(self):
        self._activo = False
        print('Luz Apagada')
        return
