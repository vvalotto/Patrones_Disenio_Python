'''
Created on 26/07/2013

@author: voval
'''

from abc import ABCMeta, abstractmethod, abstractproperty

class AbsTempCliente(metaclass=ABCMeta): 

    @abstractmethod
    def timeout(self):
        pass

    def _set_tiempo(self,value):
        pass
    def _get_tiempo(self):
        pass 
    tiempo = abstractproperty(_get_tiempo, _set_tiempo)
        