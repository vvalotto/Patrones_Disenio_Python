from enum import Enum

class Severidad(Enum):
    INFO = 0
    ALERTA  = 1
    ERROR = 2
    CRITICO = 3

class TipoError(Enum):
    INGRESO_USUARIO = 0
    INTERNO = 1
    SERVICIO = 2

class ErrorInfo(object):

    @property
    def causa(self):
        return self._causa

    @causa.setter
    def causa(self, valor):
        self._causa = valor

    @property
    def id_error(self):
        return self._id_error

    @id_error.setter
    def id_error(self, valor):
        self._id_error = valor

    @property
    def id_contexto(self):
        return self._id_contexto

    @id_contexto.setter
    def id_contexto(self, valor):
        self._id_contexto = valor

    @property
    def tipo_error(self):
        return self._tipo_error

    @tipo_error.setter
    def tipo_error(self, valor):
        self._tipo_error = valor

    @property
    def severidad (self):
        return self._severidad

    @severidad.setter
    def severidad(self, valor):
        self._severidad = valor

    @property
    def descripcion_error_usuario(self):
        return self._descripcion_error_usuario

    @descripcion_error_usuario.setter
    def descripcion_error_usuario(self, valor):
        self._descripcion_error_usuario = valor

    @property
    def descripcion_error(self):
        return self._descripcion_error

    @descripcion_error.setter
    def descripcion_error(self, valor):
        self._descripcion_error = valor

    @property
    def correccion_error(self):
        return self._correccion_error

    @correccion_error.setter
    def correccion_error(self, valor):
        self._correccion_error = valor

    def __init__(self):
        self._causa = None
        self._id_error = None
        self._id_contexto = None

        self._tipo_error = None
        self._severidad = None

        self._descripcion_error_usuario = None
        self._descripcion_error = None
        self._correccion_error = None

        self._parametros = {}

    def __repr__(self):
        retorno = ""
        retorno += "Causa: " + str(self._causa) + '\n'
        retorno += "ID Error: " + str(self._id_error) + '\n'
        retorno += "ID Contexto: " + str(self._id_contexto) + '\n'
        retorno += "Tipo Error: " + str(self._tipo_error) + '\n'
        retorno += "Severidad: " + str(self._severidad)
        return retorno


class GestorExcepcion(BaseException):

    def __init__(self):
        self.lista_error_info = []

    def agregar_info(self, info):
        self.lista_error_info.append(info)
        return info

    def obtener_lista_error_info(self):
        return self.lista_error_info
