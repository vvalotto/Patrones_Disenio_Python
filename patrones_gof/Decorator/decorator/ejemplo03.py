"""
Funcion como parametro de funciones
"""

def saludar(nombre):
    return "Hola " + nombre

def llamar_funcion(func):
    nombre = "Alejo"
    return func(nombre)


print(llamar_funcion(saludar))