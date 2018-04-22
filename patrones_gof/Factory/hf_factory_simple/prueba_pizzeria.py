from Factory.hf_factory_simple.pizzeria import *
from Factory.hf_factory_simple.factory_pizza import *

#Creo mi pizzería con una factoría de pizzas
pizzeria = Pizzeria(FactoriaSimplePizza())
#Pido una pizza de queso
pizza = pizzeria.pedir_pizza("cheese")
print("Se pidio la pizza de " + pizza.nombre)


