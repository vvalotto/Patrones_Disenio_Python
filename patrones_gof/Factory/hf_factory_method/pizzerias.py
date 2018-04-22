"""
Patron Factory Method
"""

from .pizzas import *
from abc import abstractmethod


class Pizzeria(object):
    """
    Tipo abstracto creador de tipos. El método de creación es abstracto
    y delega a las factorias concretas la creación de los objetos concretos
    """
    @abstractmethod
    def crear_pizza(self, tipo_pizza):
        pass

    def pedir_pizza(self, tipo_pizza):

        pizza = self.crear_pizza(tipo_pizza)
        print("Cocinando: " + pizza.nombre)
        pizza.preparar()
        pizza.hornear()
        pizza.cortar()
        pizza.empaquetar()
        return pizza


class ChicagoPizzeria(Pizzeria):
    """
    La pizzeria de Chicago sabe que pizzas crear
    """
    def crear_pizza(self, tipo_pizza):

        pizza = None

        if tipo_pizza == "chesse":
            pizza = PizzaChesseChicagoStyle()
        elif tipo_pizza == "clam":
            pizza = PizzaClamChicagoStyle()
        elif tipo_pizza == "veggie":
            pizza = PizzaVeggieChicagoStyle()
        elif tipo_pizza == "peperoni":
            pizza = PizzaPeperoniChicagoStyle()

        return pizza


class NYPizzeria(Pizzeria):
    """
    La pizzeria de NY sabe que pizzas crear
    """

    def crear_pizza(self, tipo_pizza):

        pizza = None

        if tipo_pizza == "chesse":
            pizza = PizzaChesseNYStyle()
        elif tipo_pizza == "clam":
            pizza = PizzaClamNYStyle()
        elif tipo_pizza == "veggie":
            pizza = PizzaVeggieNYStyle()
        elif tipo_pizza == "peperoni":
            pizza = PizzaPeperoniNYStyle()

        return pizza
