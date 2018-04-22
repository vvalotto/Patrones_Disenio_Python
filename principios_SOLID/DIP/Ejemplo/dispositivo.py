'''
Created on 25/07/2013

@author: voval
'''

from abc import ABCMeta, abstractmethod

class AbsDispositivo(metaclass=ABCMeta):
    def __init__(self):
        self._estado = False
        return
    
    @abstractmethod
    def prende(self):
        pass
    
    @abstractmethod
    def apaga(self):
        pass
    

    
    
    