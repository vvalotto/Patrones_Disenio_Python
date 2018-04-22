"""
Pizza es el producto que crea la factoría
"""


class Pizza(object):
    """
    Tipo abstracto de pizzas, que define la estructura comun de pizzas
    Esta definida como un tipo abstracto, con implementaciones que pueden ser
    sobreescritas
    """

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        return

    @property
    def masa(self):
        return self._masa

    @masa.setter
    def masa(self, valor):
        self._masa = valor
        return

    @property
    def salsa(self):
        return self._salsa

    @salsa.setter
    def salsa(self, valor):
        self._salsa = valor
        return

    @property
    def ingredientes(self):
        return self._ingredientes

    def __init__(self):
        self._ingredientes = []
        self._nombre = None
        self._masa = None
        self._salsa = None
        return

    def agregar_ingredientes(self, ingrediente):
        self._ingredientes.append(ingrediente)
        return

    def preparar(self):
        print("Preparando " + self._nombre)
        print("Amasando ...")
        print("Agregando la salsa ...")
        print("Agregando ingredientes: ")
        for ingrediente in self._ingredientes:
            print("   " + ingrediente)
        return

    def hornear(self):
        print("Hornear 25 minutos a 130 grados")
        return

    def cortar(self):
        print("Cortar la pizza en trozo")
        return

    def empaquetar(self):
        print("Poner en la caja de pizzas")
        return

    def __str__(self):
        resultado_cadena = ""
        resultado_cadena = resultado_cadena + "---- " \
                           + self._nombre + " ---\n"
        resultado_cadena = resultado_cadena\
                            + self._masa + "\n"
        resultado_cadena = resultado_cadena\
                          + self._salsa + "\n"
        return resultado_cadena



class CheesePizza(Pizza):
    """
    Tipos concretos de Pizzas, implementan el tipo abstracto: Pizza de queso
    """
    def __init__(self):
        super(CheesePizza, self).__init__()
        self.nombre = "Cheese Pizza"
        self.masa = "Regular Crust"
        self.salsa = "Marinara Pizza Sauce"

        self.agregar_ingredientes("Fresh Mozzarella")
        self.agregar_ingredientes("Parmasano")

        return


class PeperoniPizza(Pizza):
    """
    Tipos concretos de Pizzas, implementan el tipo abstracto: Pizza de Peperoni
    """
    def __init__(self):
        super(PeperoniPizza, self).__init__()
        self.nombre = "Peperoni Pizza"
        self.masa = "Crust"
        self.salsa = "Marinara Sauce"

        self.agregar_ingredientes("Sliced Pepperoni")
        self.agregar_ingredientes("Sliced Onions")
        self.agregar_ingredientes("Grated parmesan cheese")

        return

class VeggiePizza(Pizza):
    pass

class ClamPizza(Pizza):
    pass





