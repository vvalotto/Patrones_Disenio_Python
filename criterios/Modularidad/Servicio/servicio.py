'''
Created on 09/11/2013

@author: voval
'''

from abc import ABCMeta, abstractmethod

class Servicio(metaclass=ABCMeta):
    '''
    classdocs
    '''

    @abstractmethod
    def hacer(self):
        pass
        

class ServicioImp(Servicio):
    
    def hacer(self):
        print('Servicio 1')
    
