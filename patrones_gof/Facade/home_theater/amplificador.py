"""

"""

class Amplificador():

    def __init__(self, descripcion):

        self._descripcion = descripcion
        self._sintonizador = None
        self._reproductor_dvd = None
        self._reproductor_cd = None

    def on(self):

        print(self._descripcion + " prendido")
        return

    def off(self):

        print(self._descripcion + " apagado")
        return

    def poner_estereo(self):

        print(self._descripcion + " audio en esterero")
        return

    def poner_surround(self):

        print(self._descripcion + " audio en surround")
        return

    def poner_volumen(self, nivel):

        print(self._descripcion + " se puso el volumen a " + str(nivel))
        return

    def poner_sintonizador(self, sintonizador):

        print(self._descripcion + " se puso el sintonizador: " + str(sintonizador))
        return

    def poner_dvd(self, dvd):

        print(self._descripcion + " se puso el sintonizador: " + str(dvd))
        return

    def poner_cd(self, cd):

        print(self._descripcion + " se puso el sintonizador: " + str(cd))
        return

    def __str__(self):
        return self._descripcion