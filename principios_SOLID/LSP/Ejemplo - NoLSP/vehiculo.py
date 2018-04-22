'''
Created on 23/07/2013

@author: voval
'''
class Vehiculo:
    
    def __init__(self):
        pass
    
    def _get_marca(self):
        return self._marca
           
    marca = property(_get_marca)
    
    
    def _get_modelo(self):
        return self._modelo
        
    modelo = property(_get_modelo)
    
    def _get_cilindrada(self):
        return self._cilindrada
        
    cilindrada = property(_get_cilindrada)