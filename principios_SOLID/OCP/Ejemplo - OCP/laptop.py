'''
Created on 21/07/2013

@author: voval
'''
from aComputer import AbsComputer


class Laptop(AbsComputer):
    def get_computerDescription(self):
        return "Tenes una laptop"