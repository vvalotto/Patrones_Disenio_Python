'''
Created on 21/07/2013

@author: voval
'''
from forma import Forma

class Cuadrado(Forma):
    def __init__(self, lado):
        self._tipo = 1
        self._lado = lado
        return
        
        
    def Dibujar(self):
        print('Dibujando Cuadrado')
        return
