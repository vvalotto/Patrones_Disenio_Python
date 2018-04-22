"""
Closure
"""

def componer_funcion_saludar(nombre):

    def mandar_saludo():
        return "Hola a todos, soy " + nombre

    return mandar_saludo

saludar = componer_funcion_saludar("Alejo")

print(saludar())