'''
Created on 18/07/2013

@author: voval
'''

from tkinter import *

class Rectangulo():
    
    def __init__(self, rgeometrico):
        self._rectangulo = rgeometrico
        
    def dibujar(self):
        master = Tk()
        w = Canvas(master, width = 1000, height = 1000)
        w.pack()
        w.create_rectangle(100,100, 100 + self._rectangulo.base, 100 + self._rectangulo.altura)
        mainloop()
        
        