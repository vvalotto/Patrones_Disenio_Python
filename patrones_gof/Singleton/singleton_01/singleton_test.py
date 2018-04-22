from Singleton.singleton_01.singleton import *

mi_instancia = SoloUna("Solo esta instancia")
print(mi_instancia.instancia)
print(mi_instancia)

otra_instancia = SoloUna("Misma instancia")
print(otra_instancia.instancia)
print(otra_instancia)
