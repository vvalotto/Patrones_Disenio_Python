'''
Created on 21/07/2013

@author: voval
'''
from forma import Forma

class Circulo(Forma):
    def __init__(self, radio = 0):
        self._tipo = 2
        self._radio = radio
        return
    
    def Dibujar(self):
        print('Dibujando Circulo')
        return

        