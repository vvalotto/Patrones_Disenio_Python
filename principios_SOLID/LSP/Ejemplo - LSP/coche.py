'''
Created on 23/07/2013

@author: voval
'''

from vehiculo import *

class Coche(Vehiculo):
    
    def __init__(self, marca, modelo, cilindrada):
        self._marca = marca
        self._modelo = modelo
        self._cilindrada = cilindrada
        
    def obtener_id(self):
        print('Obtiene numero de Matricula')
        return 'Matricula'
