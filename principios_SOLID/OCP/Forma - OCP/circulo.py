'''
Created on 22/07/2013

@author: voval
'''

class Circulo(object):
    def __init__(self,x,y,radio):
        self.x = x
        self.y = y
        self.radio = radio
    def draw(self):
        print ("Drawing Circle at ({0},{1}) with radius {2}".
               format(self.x, self.y,self.radio))
        