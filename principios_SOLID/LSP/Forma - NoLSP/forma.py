'''
Created on 21/07/2013

@author: voval
'''

class Forma():

    def __init__(self):
        self._tipos = {1: Cuadrado, 
                       2: Circulo}
        return
    
    
    def dibujarForma(self, f):
        
        if f._tipo == 1:            
            f.Dibujar()
        elif f._tipo == 2:
            f.Dibujar()
        else:
            print('Nada para dibujar')
        
        return   