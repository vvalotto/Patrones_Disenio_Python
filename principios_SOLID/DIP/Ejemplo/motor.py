'''
Created on 25/07/2013

@author: voval
'''

class Motor:
    def __init__(self):
        self._activo = False
        return
        
    def prende(self):
        self._activo = True
        print('Motor Prendido')
        return
        
    def apaga(self):
        self._activo = False
        print('Motor Apagado')
        return
