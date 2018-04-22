"""

"""

class Pantalla():

    def __init__(self, descripcion):

        self._descripcion = descripcion
        return

    def abrir(self):

        print(self._descripcion + " abierto")
        return

    def cerrar(self):

        print(self._descripcion + " cerrado")
        return

    def __str__(self):
        return self._descripcion