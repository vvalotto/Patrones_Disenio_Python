'''
Created on 22/07/2013

@author: voval
'''

class Cuadrado(object):
    def __init__(self,x,y,lado):
        self.x = x
        self.y = y
        self.lado = lado
    def draw(self):
        print ("Drawing Cuadrado at ({0},{1}) with lado {2}".
               format(self.x, self.y,self.lado))
        