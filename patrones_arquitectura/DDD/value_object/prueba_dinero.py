from DDD.value_object.dinero import *


mi_dinero = Dinero(100)
dinero_prestado = Dinero(200)
otro_dinero = Dinero(100, Moneda.Dolares)

mi_dinero = mi_dinero.sumar(dinero_prestado)

print(mi_dinero.monto)

print(mi_dinero == otro_dinero)

print(mi_dinero)

d1 = Dinero(30)
d2 = Dinero(40)
d3 = d1 + d2
print(d3)