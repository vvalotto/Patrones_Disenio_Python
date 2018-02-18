class TipoZ(object):
     mi_atributo = ''

     @staticmethod
     def mostrar_atributo():
         print(TipoZ.mi_atributo)

class tipoY(object):

    def __init__(self):
        print('Tipo X Creado')

    def hacer(self):
        print('Tipo X hace algo')
        return

class tipo(object):

    def __init__(self):
        self._tipo_x = tipoX()

    def hacer(self):
        self._tipo_x.hacer()
        print('tipo Y hace algo')

    def hacer_otra_cosa(self):
        TipoZ.mi_atributo = 'El atributo'
        TipoZ.mostrar_atributo()


if __name__ == '__main__':

    tipo_y = tipoY()
    tipo_y.hacer()
    tipo_y.hacer_otra_cosa()
