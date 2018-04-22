'''
Created on 07/01/2014

@author: vvalotto
'''

class Rectangulo():


    def _get_altura(self):
        return self._altura
    
    def _set_altura(self, valor):
        self._altura = valor
        
    def _get_base(self):
        return self._base
    
    def _set_base(self, valor):
        self._base = valor
    
    altura = property(_get_altura, _set_altura)
    base = property(_get_base, _set_base)
    
    def area(self):
        return self._base * self._altura
    

class Cuadrado(Rectangulo):
    
    def _set_altura(self,valor):
        Base.altura = valor
        Base.base = valor
        
    def _set_base(self,valor):
        Base.altura = valor
        Base.base = valor

        
    
    
        