'''
Created on 09/11/2013

@author: voval
'''
from dispositivo import *

class Funcion(object):

    def __init__(self, dispositivo):
        self.dispositivo = dispositivo

    def pagar_uso(self):
        return self.dispositivo.precio * ( 1 - self.dispositivo.obtener_descuento()) 
        