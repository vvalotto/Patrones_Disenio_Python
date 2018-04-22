'''
Created on 23/07/2013

@author: voval
'''

from coche import Coche
from ciclomotor import Ciclomotor

class Impuesto():
    
    def _serv_calculo_impuesto(self, matricula, cilindrada):
        print('Matricula:')
        print(cilindrada)
        return
    

    
    def calcular(self, vehiculo):
        
        if type(vehiculo) == Coche:
            matricula = vehiculo.obtener_matricula()
        elif type(vehiculo) == Ciclomotor:
            matricula = vehiculo.obtener_num_licencia()
        print(vehiculo.cilindrada)

        self._serv_calculo_impuesto(matricula, vehiculo.cilindrada)
        return

        

        
        