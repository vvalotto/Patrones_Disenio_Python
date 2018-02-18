from abc import ABCMeta, abstractmethod


class TipoY(metaclass=ABCMeta):

    def __init__(self):
        self._dato = 'inicio'
        return

    @abstractmethod
    def hacer(self):
        pass


class TipoX(TipoY):

    def __init__(self):
        super().__init__()
        self.accion = 'creando'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self.accion))
        return
    '''
    def hacer(self):
        self.accion = 'haciendo algo'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self.accion))
        return
        pass
   '''

if __name__ == '__main__':
    x = TipoX()
    x.hacer()
    print(x._dato)