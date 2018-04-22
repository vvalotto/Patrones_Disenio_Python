'''
Created on 18/07/2013

@author: voval
'''

from tkinter import *

class Rectangulo:
    
    def __init__(self, base=0, altura=0):
        self._base = base
        self._altura = altura
        
    def _get_base(self):
        return self._base

    def _set_base(self, valor):
        self._base = valor

    def _get_altura(self):
        return self._altura

    def _set_altura(self, valor):
        self._altura = valor
        
    altura = property(_get_altura, _set_altura)
    base = property(_get_base, _set_base)   
    
    def perimetro(self):
        return (2 * self._base + 2 * self._altura)
    
    def area(self):
        return (self._base * self._altura)
    
    def dibujar(self):
        master = Tk()
        w = Canvas(master, width = 1000, height = 1000)
        w.pack()
        w.create_rectangle(100,100, 100 + self.base, 100 + self.altura)
        mainloop()
        
        