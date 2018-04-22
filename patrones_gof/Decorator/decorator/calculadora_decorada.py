from Decorator.decorator.mi_decorador import *

class Calculadora(object):
    @log_ingresa_funcion
    @log_errores
    @log_temporizar
    def suma(self, x, y):
        return x + y

    @log_ingresa_funcion
    @log_errores
    def div(self, x, y):
        return x / y

    @log_ingresa_funcion
    @log_errores
    def suma_lista(self, lista):
        lista_doble = [x * 2 for x in lista]
        return sum(lista_doble)

calc = Calculadora()

print(calc.suma(3, 4))
print(calc.div(10, 0))
print(calc.suma_lista([4, 6, 7, 9]))