"""

"""

class Proyector():

    def __init__(self, descripcion, reproductor_dvd):

        self._descripcion = descripcion
        self._reproductor_dvd = reproductor_dvd
        return

    def on(self):

        print(self._descripcion + " prendido")
        return

    def off(self):

        print(self._descripcion + " apagado")
        return

    def poner_modo_widescreen(self):

        print(self._descripcion + " pantalla en widescreen (16x9)")
        return

    def poner_modo_tv(self):

        print(self._descripcion + " pantalla en modo tv (4x3)")
        return

    def __str__(self):
        return self._descripcion