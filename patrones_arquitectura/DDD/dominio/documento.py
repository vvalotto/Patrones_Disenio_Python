"""
Objeto Valor Documento
"""
from abc import *
from .objeto_valor import *


class ValidadorDocumentoFactory:

    @staticmethod
    def crear_validador(tipo_documento):

        if tipo_documento == "DNI":
            return ValidadorDNI()
        elif tipo_documento == "CUIT":
            return ValidadorCUIT()
        elif tipo_documento == "CUIL":
            return ValidadorCUIL()
        elif tipo_documento == "Pasaporte":
            return ValidadorPasaporte()
        elif tipo_documento == "LC":
            return ValidadorLibretaCivica()

        raise ErrorTipoDocumentoInvalido()

        pass


class ErrorTipoDocumentoInvalido(Exception):

    def __init__(self):
        print("El tipo de documento no es correcto")
        return


class ValidadorDocumento(metaclass=ABCMeta):

    @abstractstaticmethod
    def validar(self, numero):
        pass


class ValidadorDNI(ValidadorDocumento):

    def validar(self, numero):

        if numero is None:
            return False

        if type(numero) != int:
            return False

        return True


class ValidadorCUIT(ValidadorDocumento):

    def validar(self, numero):

        if numero is None:
            return False

        return True


class ValidadorCUIL(ValidadorDocumento):

    def validar(self, numero):

        if numero is None:
            return False

        return True


class ValidadorPasaporte(ValidadorDocumento):

    def validar(self, numero):

        if numero is None:
            return False

        return True


class ValidadorLibretaCivica(ValidadorDocumento):

    def validar(self, numero):

        if numero is None:
            return False

        return True


class Documento(ObjetoValor):

    @property
    def tipo_documento(self):
        return self._tipo_documento

    @property
    def numero(self):
        return self._numero

    def __init__(self, tipo_documento, numero):

        if not self._validar_tipo_documento(tipo_documento, numero):
            raise DocumentoNoValido()

        self._numero = numero
        self._tipo_documento = tipo_documento
        return

    @staticmethod
    def _validar_tipo_documento(tipo_documento, numero):
        return ValidadorDocumentoFactory.crear_validador(tipo_documento).validar(numero)

    def __str__(self):
        return str(self._tipo_documento) + ": " + str(self._numero)

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._tipo_documento, self._numero]


class DocumentoNoValido(Exception):

    def __init__(self):
        print("Documento No Valido")
        return
