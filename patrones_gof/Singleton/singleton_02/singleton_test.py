from Singleton.singleton_02.singleton import *

instancia = MiSingleton()
print(instancia.get_instance())
instancia.agregar_recurso('1', 1)
print(instancia.get_recursos())


