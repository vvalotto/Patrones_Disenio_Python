"""

"""

class Luces():

    def __init__(self, descripcion):

        self._descripcion = descripcion
        return

    def on(self):

        print(self._descripcion + " prendido")
        return

    def off(self):

        print(self._descripcion + " apagado")
        return

    def atenuar(self, nivel):

        print(self._descripcion + " atenuado " + str(nivel) + "%")
        return

    def __str__(self):
        return self._descripcion