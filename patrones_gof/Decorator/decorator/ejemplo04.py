"""
Funciones que retornan funciones
"""

def componer_funcion_saludar():

    def mandar_saludo():
        return "Hola a todos"

    return mandar_saludo

saludar = componer_funcion_saludar()

print(saludar())