
class Singleton(object):
    variable = 'Tengo solo una variable'
    def __new__(cls):
        if not hasattr(cls, 'instancia'):
            cls.instancia = super(Singleton, cls).__new__(cls)
        return cls.instancia
