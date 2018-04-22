'''
Created on 21/07/2013

@author: voval
'''
from servidor import *

class Cliente:
    def __init__(self, nombre, servidor):
        self._servidor = servidor
        self._nombre = nombre
        
    def Saludar(self):
        self._servidor.Saludar(self._nombre)
        
        