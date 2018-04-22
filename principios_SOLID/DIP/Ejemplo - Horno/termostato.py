'''
Created on 25/07/2013

@author: voval
'''
import time
from termometro import *

class Termostato:
    def __init__(self):
        self.TERMOMETRO = 86
        self.HORNO = 87
        self.ACOPLE = True
        self.DESACOPLE = False
        self.termo = Termometro()
        print('Inicio')
        
        return
    
    def regular(self, min_temp, max_temp):       
     
        lectura = self.ingresar()   
        while True:
     
            while (lectura < max_temp):
                print(lectura)
                lectura = self.ingresar()
            termo.cambiar_temp(self.DESACOPLE)
        
            while (lectura > min_temp):
                print(lectura)
                lectura = self.ingresar()
            termo.cambiar_temp(self.ACOPLE)
            

        return
    
    def ingresar(self):
        return self.termo.leer_temp()
            
        
        
    