"""
Programa Principal para hacer pedidos de cafe
"""

from Decorator.hf_starbuzz.bebida import *
from Decorator.hf_starbuzz.condimentos import *

bebida = Expresso()
print("Estoy pidiendo: " + bebida.pedir_descripcion())
print("")

otra_bebida = DarkRoast()
otra_bebida = Mocha(otra_bebida)
otra_bebida = Mocha(otra_bebida)
otra_bebida = Whip(otra_bebida)
print("Estoy pidiendo: " + otra_bebida.pedir_descripcion())
print("")

mi_bebida = HouseBlend()
mi_bebida = Soy(mi_bebida)
mi_bebida = Mocha(mi_bebida)
mi_bebida = Whip(mi_bebida)
print("Estoy pidiendo: " + str(mi_bebida.costear()))



