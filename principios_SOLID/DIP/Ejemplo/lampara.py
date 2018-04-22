'''
Created on 24/07/2013

@author: voval
'''

class Lampara:
    def __init__(self):
        self._activo = False
        return
        
    def prende(self):
        self._activo = True
        print('Luz Pendida')
        return
        
    def apaga(self):
        self._activo = False
        print('Luz Apagada')
        return

        