'''
Created on 21/07/2013

@author: voval
'''

from abc import ABCMeta, abstractmethod

class AbsComputer:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_computerDescription(self):
        pass