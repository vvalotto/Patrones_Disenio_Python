'''
Created on 26/07/2013

@author: voval
'''

from abc import ABCMeta, abstractmethod
from temp_cliente import *

class AbsPuerta(AbsTempCliente, metaclass=ABCMeta):
    
    @abstractmethod
    def bloquear(self):
        pass
    
    @abstractmethod
    def desbloquear(self):
        pass
    
    @abstractmethod
    def puerta_abierta(self):
        pass
    