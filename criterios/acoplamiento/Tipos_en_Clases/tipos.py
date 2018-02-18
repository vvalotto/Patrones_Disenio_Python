"Herencia"


class tipoZ(object):

    def __init__(self):
        print('Tipo Z Creado')

    def hacer(self, valor):
        print("El tipo Z muestra {0}".format(valor))


class tipoX(object):

    def __init__(self):
        print('Tipo X Creado')

    def hacer(self):
        print('Tipo X hace algo')
        return


class subtipoX(tipoX):

    def __init__(self):
        super().__init__()
        print('Subtipo X Creado')

class tipoY(object):

    def __init__(self):
        self._tipo_x = tipoX()

    def hacer(self):
        self._tipo_x.hacer()
        print('tipo Y hace algo')

    def hacer_otra_cosa(self, item):
        valor = 10
        item.hacer(valor)

    def mostrar_algo(self, algo):
        print(algo.__class__.__name__)


if __name__ == '__main__':

    subtipoX =subtipoX()
    tipo_z = tipoZ()
    tipo_y = tipoY()
    tipo_y.hacer()
    tipo_y.hacer_otra_cosa(tipo_z)
    tipo_y.mostrar_algo(tipo_z)