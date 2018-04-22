'''
Created on 25/07/2013

@author: voval
'''

class Boton:
    def __init__(self, disp):
        self._estado = False
        self.disp = disp
        return
    
    def Presionar(self,disp):
        
        if self._estado:
            self.disp.apaga()
        else:
            self.disp.prende()
            
        self._estado = not self._estado
        return