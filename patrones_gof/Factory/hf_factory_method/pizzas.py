"""
El producto que se crea mediante la factoria es Pizza
"""


class Pizza(object):
    """
    Tipo abstracto de pizzas, que define la estructura comun de pizzas
    Este tipo es lo que produce la factoría: una pizza
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


class PizzaVeggieChicagoStyle(Pizza):
    """
    Implementación de una clase concreta del producto a crear
    """

    def __init__(self):
        super(PizzaVeggieChicagoStyle, self).__init__()
        self.nombre = "Chicago Deep Dish Veggie Pizza"
        self.masa = "Extra Thick Crust Dough"
        self.salsa = "Plum Tomato Sauce"

        self.agregar_ingredientes("Shredded Mozzarella Cheese")
        self.agregar_ingredientes("Black Olives")
        self.agregar_ingredientes("Spinach")
        self.agregar_ingredientes("Eggplant")

        return

    def cortar(self):
        print(" Cortar en pedazos cuadrados")
        return


class PizzaPeperoniChicagoStyle(Pizza):
    def __init__(self):
        super(PizzaPeperoniChicagoStyle, self).__init__()
        self.nombre = "Chicago Deep Dish Peperoni Pizza"
        self._masa = "Extra Thick Crust Dough"
        self._salsa = "Plum Tomato Sauce"

        self.agregar_ingredientes("Shredded Mozzarella Cheese")
        self.agregar_ingredientes("Black Olives")
        self.agregar_ingredientes("Spinach")
        self.agregar_ingredientes("Eggplant")
        self.agregar_ingredientes("Sliced Pepperoni")

        return

    def cortar(self):
        print(" Cortar en pedazos cuadrados")
        return


class PizzaClamChicagoStyle(Pizza):
    pass


class PizzaChesseChicagoStyle(Pizza):
    pass


class PizzaChesseNYStyle(Pizza):
    pass


class PizzaClamNYStyle(Pizza):
    pass


class PizzaVeggieNYStyle(Pizza):
    pass


class PizzaPeperoniNYStyle(Pizza):
    pass

