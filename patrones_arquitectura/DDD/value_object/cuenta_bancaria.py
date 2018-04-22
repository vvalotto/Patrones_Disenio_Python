from enum import *

class CuentaBancaria:

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor
        return

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, valor):
        self._balance = valor
        return

    def __init__(self, GUID, balance_inicial):

        self._id = GUID
        self._balance = balance_inicial

        return


class Dinero:

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, valor):
        self._monto = valor
        return

    @property
    def moneda(self):
        return self._moneda

    @moneda.setter
    def moneda(self, valor):
        self._moneda = valor
        return

    def __init__(self, monto, moneda):
        self._monto = monto
        self._moneda = moneda


class Moneda(Enum):
    Dolares = 1
    Pesos = 2
    Libras = 3
