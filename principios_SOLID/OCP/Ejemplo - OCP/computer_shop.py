'''
Created on 21/07/2013

@author: voval
'''

class ComputerShop:
    def __init__(self):
        self.miComp = None
        pass
    
    def get_myComputerDescription(self, tipoComp):
        self.miComp = tipoComp
        return tipoComp.get_computerDescription(self)
        

