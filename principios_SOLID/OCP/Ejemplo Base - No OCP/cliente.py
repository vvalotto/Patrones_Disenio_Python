'''
Created on 05/01/2014

@author: vvalotto
'''

from mi_servidor import * 

class Cliente:
    def __init__(self,cliente):
        print(cliente)
        print('-----')
        s = MiServidor()
        s.Saludar(cliente)