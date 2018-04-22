"""
Ejemplo de manejo de estado con una resolución sin patrones
"""

class Dispositivo(object):

    OFF = 0
    ON = 1
    TRABAJANDO = 2

    def __init__(self):
        self._estado = Dispositivo.OFF
        return

    def prender(self):

        if self._estado == Dispositivo.OFF:
            self._estado = Dispositivo.ON
            print('El dispositivo se prendio')
        else:
            print('El dispositivo ya está prendido')
        return

    def apagar(self):

        if self._estado == Dispositivo.ON:
            self._estado = Dispositivo.OFF
            print('El dispositivo se apago')
        elif self._estado == Dispositivo.TRABAJANDO:
            self._estado = Dispositivo.OFF
            print('El dispositivo se apago')
        else:
            print('El dispositivo ya está apagado')
        return

    def iniciar(self):

        if self._estado == Dispositivo.ON:
            self._estado = Dispositivo.TRABAJANDO
            print('El dispositivo se inicio')
        elif self._estado == Dispositivo.TRABAJANDO:
            print('El dispositivo esta trabajando')
        else:
            print('El dispositivo esta apagado y no puede trabajar')
        return



if __name__ == '__main__':
    disp = Dispositivo()
    disp.prender()
    disp.iniciar()
    disp.iniciar()
    disp.prender()
    disp.apagar()
