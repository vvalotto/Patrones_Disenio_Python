import math

class Salida(object):

    direccion = ""
    Indicador = ""
    posicion = None


class Comparador(object):

    def __init__(self, referencia):
        self._referencia = referencia

    def comparar(self, posicion):

        resultado = "Quieto"
        if posicion != self._referencia:
            resultado = "Subir" if posicion < self._referencia else "Bajar"
        return resultado

class Actuador(object):

    def __init__(self, tope1, tope2):
        self._tope1 = tope1
        self._tope2 = tope2

    def actuar(self, direccion):
        print(direccion)

    def alertar(self, posicion):
        if math.fabs(posicion - self._tope1) > 2:
            Indicador = "Apagado"
        else:
            Indicador = "Prendido"
        return Indicador


class Control(object):

    def __init__(self):
        self.mi_comparador = Comparador(10)
        self.mi_actuador = Actuador(15, 5)

    def mover(self, salida):
        salida.Indicador = self.mi_actuador.alertar(salida.posicion)
        print(salida.Indicador)
        self.mi_actuador.actuar(self.mi_comparador.comparar(salida.posicion))


if __name__ == "__main__":
    mi_salida = Salida()
    mi_salida.posicion = 7
    mi_control = Control()
    mi_control.mover(mi_salida)