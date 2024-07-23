class ManejadorOrdenes:
    def manejar(self, orden, es_prioritaria):
        if es_prioritaria:
            return self._manejar_prioritaria(orden)
        else:
            return self._manejar_regular(orden)

    def _manejar_prioritaria(self, orden):
        # Lógica para manejar una orden prioritaria
        return f"Orden prioritaria procesada: {orden}"

    def _manejar_regular(self, orden):
        # Lógica para manejar una orden regular
        return f"Orden regular procesada: {orden}"

class ProcesadorOrdenes:
    def __init__(self, manejador):
        self.manejador = manejador

    def procesar(self, orden, es_prioritaria):
        resultado = self.manejador.manejar(orden, es_prioritaria)
        print(resultado)

manejador = ManejadorOrdenes()
procesador = ProcesadorOrdenes(manejador)
procesador.procesar("Orden123", True)
procesador.procesar("Orden456", False)