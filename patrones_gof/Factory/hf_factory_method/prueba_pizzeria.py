
from Factory.hf_factory_method.pizzerias import *

#Crear la pizzeria
pizzeria_chicago = ChicagoPizzeria()

#Hace el pedido 1
pizza = pizzeria_chicago.pedir_pizza("veggie")
print("Pepe pidio " + pizza.nombre)

#Hace el pedido 2
pizza = pizzeria_chicago.pedir_pizza("peperoni")
print("María pidio " + pizza.nombre)
