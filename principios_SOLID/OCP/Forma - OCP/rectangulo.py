'''
Created on 22/07/2013

@author: voval
'''

class Rectangulo(object):
    def __init__(self,x,y,lado1,lado2):
        self.x = x
        self.y = y
        self.lado1 = lado1
        self.lado2 = lado2
    def draw(self):
        print ("Drawing Cuadrado at ({0},{1}) with lado1 {2} y lado 2 {3}".
               format(self.x, self.y,self.lado1, self.lado2))
        