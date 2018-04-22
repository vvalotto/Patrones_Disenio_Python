class Contenedor(object):

    __INSTANCE = None

    class Singleton:
        def __init__(self):
            self.__lista_recursos = {}

        def agregar_recurso(self, clave, valor):
            self.__lista_recursos[clave] = valor
            return

        def get_recursos(self):
            return self.__lista_recursos

    def __init__(self):
        if self.__INSTANCE is not None:
            raise ValueError('Ya hay una instancia')

    @classmethod
    def get_instance(cls):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = Contenedor.Singleton()
        return cls.__INSTANCE

