"""
Factoría de los tipos pizzas
"""

from .pizzas import *


class FactoriaSimplePizza():

    @staticmethod
    def crear_pizza(tipo_pizza):
        """
        Metodo para la creacion del tipo de pizza solicitado
        No es necesario intanciar la factoría, por lo tanto el método
        es estático
        :param tipo_pizza: Referencia al tipo de pizza
        :return: pizza
        """

        pizza = None

        if tipo_pizza == "cheese":
            pizza = CheesePizza()
        elif tipo_pizza == "peperoni":
            pizza = PeperoniPizza()
        elif tipo_pizza == "clam":
            pizza = ClamPizza()
        elif tipo_pizza == "veggie":
            pizza = VeggiePizza()

        print("Se creo: " + str(pizza))
        return pizza


