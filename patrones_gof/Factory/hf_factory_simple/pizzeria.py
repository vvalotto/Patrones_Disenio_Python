"""
La pizzeria es la que usa a la factoria para crear la pizza y luego
hacerla
"""

class Pizzeria(object):

    def __init__(self, factoria):
        self._factoria = factoria
        return

    def pedir_pizza(self, tipo_pizza):

        pizza = self._factoria.crear_pizza(tipo_pizza)

        pizza.preparar()
        pizza.hornear()
        pizza.cortar()
        pizza.empaquetar()

        return pizza
