from DDD.value_object.objeto_valor import *
from enum import *

class Moneda(Enum):
    Dolares = 1
    Pesos = 2
    Libras = 3


class Dinero(ObjetoValor):

    @property
    def monto(self):
        return self._monto

    @property
    def moneda(self):
        return self._moneda

    def __init__(self, monto=0, moneda=Moneda.Pesos):
        self._monto = monto
        self._moneda = moneda
        return

    @staticmethod
    def crear(monto):
        if (monto % 0.01 != 0):
            raise Exception()

        if monto < 0 :
            raise Exception()

        return Dinero(monto)

    def sumar(self, dinero):
        return Dinero(self.monto + dinero.monto, dinero.moneda)

    def restar(self, dinero):
        return Dinero(self.monto - dinero.monto, dinero.moneda)

    def __add__(self, otro):
        return Dinero(self._monto + otro._monto)

    def __sub__(self, otro):
        return Dinero(self._monto - otro._monto)

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._monto, self._moneda]

    def _validar(self, monto):
        if (monto % 0.01 != 0):
            raise Exception()

        if monto < 0 :
            raise Exception()
        return

    def __str__(self):
        return str(self._monto) + ' - ' + str(self._moneda)


class MasDeDosPosicionesDecimalesMontoDineroEx(Exception):

    def __init__(self):
        pass

class MontoDineroNoPuedeSerNegativoEX(Exception):
    def __init__(self):
        pass
