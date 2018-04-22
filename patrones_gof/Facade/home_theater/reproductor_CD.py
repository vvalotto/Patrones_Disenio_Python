"""
Reproductor de CD
"""
from overloading import *

class ReproductorCD:

    def __init__(self, descripcion, amplicador):

        self._descripcion = descripcion
        self._amplificador = amplicador
        self._titulo = None
        self._pista_actual = 0

    def on(self):

        print(self._descripcion + " prendido")
        return

    def off(self):

        print(self._descripcion + " apagado")
        return

    def sacar_cd(self):

        self._titulo = None
        print(self._descripcion + " sacar cd")
        return

    @overloaded
    def reproducir(self, titulo):

        self._titulo = titulo
        self._pista_actual = 0
        print(self._descripcion + " reproduciendo: " + titulo)
        return

    @overloads(reproducir)
    def reproducir(self, pista:int):

        if self._titulo is None:
            print(self._descripcion + " no se puede reproducir " +
                  str(self._pista_actual) + ", no hay CD."
                  )
        else:
            self._pista_actual = pista
            print(self._descripcion + " reproduciendo la pista " +
                  str(self._pista_actual)
                  )
        return

    def parar(self):

        self._pista_actual = 0
        print(self._descripcion + " parado")
        return

    def pausar(self):

        print(self._descripcion + " pausado ")
        return

    def __str__(self):
        return self._descripcion