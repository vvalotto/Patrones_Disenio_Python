"""

"""

class Sintonizador():

    def __init__(self, descripcion, amplificador):

        self._descripcion = descripcion
        self._amplificador = amplificador

    def on(self):

        print(self._descripcion + " prendido")
        return

    def off(self):

        print(self._descripcion + " apagado")
        return

    def ponr_frecuencia(self, frecuencia):

        print(self._descripcion + " se puso la frecuencia en " + str(frecuencia))
        return

    def poner_am(self):

        print(self._descripcion + " esta en AM")
        return

    def poner_fm(self, dvd):

        print(self._descripcion + " esta en AM")
        return

    def __str__(self):
        return self._descripcion
