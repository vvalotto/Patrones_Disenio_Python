'''
Created on 24/11/2013

@author: voval
'''

class LectorSenial(object):
    '''
    classdocs
    '''


    def __init__(self):
        self._valores = []
    
    def leer_dato(self):
        dato = input('Valor:')
        while not(dato.isnumeric()):
            print('Dato mal ingresado, <enter>')
            dato = input('Valor:')
        return dato
    
    def leer_senial(self):
        for i in range(10):
            self._valores.append(self.leer_dato())
        return
    
    def guardar_senial_leida(self):
        fsenial = open("/Users/voval/senial.dat","a")
        for valor in self._valores:
            fsenial.write(str(valor)+'\n')
        fsenial.close()
        return
    
    def mostrar_señal(self):
        for valor in self._valores:
            print(valor)
        return