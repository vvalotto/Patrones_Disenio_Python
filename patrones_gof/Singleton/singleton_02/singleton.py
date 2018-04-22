class MiSingleton(object):

    __INSTANCE = None
    __lista_recursos = {}

    def __init__(self):
        if self.__INSTANCE is not None:
            raise ValueError('Ya hay una instancia')

    @classmethod
    def get_instance(cls):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = MiSingleton()
        return cls.__INSTANCE

    @classmethod
    def agregar_recurso(cls, clave, valor):
        cls.__lista_recursos[clave] = valor
        return

    @classmethod
    def get_recursos(cls):
        return cls.__lista_recursos
