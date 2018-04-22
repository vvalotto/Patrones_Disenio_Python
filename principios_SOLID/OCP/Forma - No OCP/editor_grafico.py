'''
Created on 21/07/2013

@author: voval
'''
import forma

class EditorGrafico():
    
    def __init__(self):
        pass
    
    def _dibujarCirculo(self, f):
        print ('Dibujo un Circulo con radio {0:2d}'.format(f._radio))
        
    def _dibujarCuadrado(self, f):
        print('Dibujo un Cuadrado con lado {0:2d}', format(f._lado))
    
    def dibujarForma(self, f):
        
        if f._tipo == 1:
            self._dibujarCuadrado(f)
        elif f._tipo == 2:
            self._dibujarCirculo(f)
        else:
            print('Nada para dibujar')
        
        return



        

         
            