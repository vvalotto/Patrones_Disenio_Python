'''
Created on 26/07/2013

@author: voval
'''
from temp_cliente import *

class Temporizador(object):
    
    def registrar(self, timeout, cliente):
        print('El tiempo paso')
        cliente.tiempo = timeout
        return
    
    