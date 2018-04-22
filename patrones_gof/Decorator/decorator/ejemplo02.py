"""
Funciones internas
"""
def saludar(nombre):

    def mandar_saludo():
        return "Hola "
    return mandar_saludo() + nombre



print(saludar("Alejo"))