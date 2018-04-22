'''
Clase Abstracta que define los metodos claves
de la especificacion
'''




class BaseEspecificacion():

    def __init__(self, objeto):
        self._objeto = objeto
        return

    def es_satifecho_por(self, objeto):
        pass


    def y(self, especificacion):
        pass


    def o(self, especificacion):
        pass


    def no(self, especificacion):
        pass

'''
Clase Abstracta que implemneta y(), o(), no()
'''


class BaseEspecificacionCompuesta(BaseEspecificacion):


    def y(self, especificacion):
        return Y_especificacion(self, especificacion)

    def o(self, especificacion):
        return O_especificacion(self, especificacion)

    def no(self, especificacion):
        return NO_especificacion(especificacion)



class Y_especificacion(BaseEspecificacionCompuesta):

    def __init__(self, espec_izquierda, espec_derecha):
        self._espec_izquierda = espec_izquierda
        self._espec_derecha = espec_derecha
        return

    def es_satifecho_por(self, objeto):
        return self._espec_izquierda.es_satisfecho_por(objeto) and\
               self._espec_derecha.es_satisfecha_por(objeto)

class O_especificacion(BaseEspecificacionCompuesta):

    def __init__(self, espec_izquierda, espec_derecha):
        self._espec_izquierda = espec_izquierda
        self._espec_derecha = espec_derecha
        return

    def es_satifecho_por(self, objeto):
        return self._espec_izquierda.es_satisfecho_por(objeto) or\
               self._espec_derecha.es_satisfecha_por(objeto)


class NO_especificacion(BaseEspecificacionCompuesta):

    def __init__(self, espec):
        self._espec = espec
        return

    def es_satifecho_por(self, objeto):
        return not(self._espec.es_satisfecho_por(objeto))
