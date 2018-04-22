'''
Created on 05/01/2014

@author: vvalotto
'''

from rectangulo import *

r = Rectangulo()
r.base = 10
r.altura = 30
print('Para un rectangulo con:')
print('Base: ' + str(r.base))
print('Altura: ' + str(r.altura))
print('Tiene un perimetro de: ' + str(r.perimetro()))
print('Tiene un area de: ' + str(r.area()))


if __name__ == '__main__':
    pass