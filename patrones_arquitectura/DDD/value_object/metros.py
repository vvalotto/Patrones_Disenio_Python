"""
Muestra como validar la igualdad de los
OV
"""
from .objeto_valor import *


class Metros(ObjetoValor):

    @property
    def distancia_en_metros(self):
        return self._distancia_en_metros

    def __init__(self, distancia_en_metros):
        if distancia_en_metros < float(0.0):
            raise DistanciaEnMetrosNoSonNegativas()

        self._distancia_en_metros = distancia_en_metros

    def en_yardas(self):
        return Yardas(self._distancia_en_metros * float(1.0936133))

    def en_kilometros(self):
        return Kilometros(self._distancia_en_metros/1000)

    def agregar(self, metros):
        return Metros(self._distancia_en_metros + metros.distancia_en_metros)

    def es_mayor_que(self, metros):
        return self._distancia_en_metros > metros.distancia_en_metros

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self.distancia_en_metros]

class Yardas():

    @property
    def distancia_en_yardas(self):
        return self._distancia_en_yardas

    def __init__(self, distancia_en_yardas):
        if distancia_en_yardas < float(0.0):
            raise DistanciaEnMetrosNoSonNegativas()

        self._distancia_en_yardas = distancia_en_yardas


class Kilometros():

    def __init__(self, distancia_en_kilometros):
        pass


class DistanciaEnMetrosNoSonNegativas(Exception):
    print('Distancias Negativas')
    pass
