'''
Created on 24/11/2013

@author: voval
'''
import pickle
from senial import *
from abc import ABCMeta, abstractmethod

class aRepositorioSenial(metaclass=ABCMeta):

    @abstractmethod
    def guardar_senial(self, senial):
        pass
    
    @abstractmethod
    def obtener_senial(self):
        pass        

class RepositorioSenialArchivo(aRepositorioSenial):
    
    def guardar_senial(self,senial):
        fsenial = open("/Users/voval/senial.dat","a")
        for valor in senial._valores:
            fsenial.write(str(valor)+'\n')
        fsenial.close()
        return    
    
    def obtener_senial(self):
        valores = []
        fsenial = open("/Users/voval/senial.dat","r")
        for dato in fsenial:
            valores.append(int(dato))
        fsenial.close()
        return valores  
        

class RepositorioSenialPickle(aRepositorioSenial):
    
    def guardar_senial(self, senial):
        psenial = open("/Users/voval/senial.pkl","wb")
        pickle.dump(senial, psenial)
        psenial.close()
        return
    
    def obtener_senial(self):
        with open("/Users/voval/senial.pkl","rb") as psenial:
            self._senial = pickle.load(psenial)
            psenial.close()
        return self._senial
