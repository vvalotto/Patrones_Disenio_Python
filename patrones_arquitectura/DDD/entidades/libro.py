'''
Definición de una entidad
'''

class Libro:
    """
    Definición de la entidad libro
    Solo tiene atributos donde uno
    es un objeto valor
    """
    @property
    def id(self):
        return self._id

    @property
    def isbn(self):
        return self._ISBN

    def __init__(self, isbn):
        self._ISBN = isbn
        self._id = isbn.numero
        return


class ISBN:
    """
    Objeto Valor. El objeto no tiene id
    """

    @property
    def numero(self):
        return self._numero

    def __init__(self, isbn):
        self._validar(isbn)
        self._numero = isbn

    def _validar(self, isbn):
        if (len(isbn) != 13 and len(isbn) != 10):
            raise Exception("ISBN debe ser de 10 o 13 digitos")

        for c in isbn:
            try:
                convertir_a_entero = int(c)
            except:
                raise Exception("ISBN debe tener solo digitos")