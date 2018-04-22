'''
Created on 24/11/2013

@author: voval
'''

from abc import ABCMeta, abstractmethod

class aSenial(metaclass=ABCMeta):
    '''
    classdocs
    '''

    @abstractmethod
    def inicializar(self):
        pass
    
    @abstractmethod
    def limpiar(self):
        pass
    
   
    @abstractmethod
    def llenar(self):
        pass

    @abstractmethod
    def obtener(self):
        pass

    @abstractmethod
    def volcar(self):
        pass

class SenialSimple(aSenial):
     
    def inicializar(self):
        self._tamanio = 10
        self._valores = []
        return

    def limpiar(self):
        self._valores.clear()
        return

    def llenar(self, dato):
        if (len(self._valores) < self._tamanio):
            self._valores.append(dato)
            return True
        else:
            return False

    def obtener(self):
        return self._valores

    def volcar(self,datos):
        for dato in datos:
            self.llenar(dato)
        return

class SenialConCanales(aSenial):
     
    def inicializar(self, tamanio, canales):
        self._tamanio = tamanio
        self._canales = canales
        self._valores = [[0 for x in range(tamanio)] for x in range(canales)]
 

    def limpiar(self):
        self._valores.clear()
        return

    def llenar(self, dato, canal):
        if (len(self._valores) < self._tamanio):
            self._valores[canal].append(dato)
            return True
        else:
            return False

    def obtener(self):
        return self._valores

    def volcar(self,datos):
        for dato in datos:
            self.llenar(dato)
        return  

        