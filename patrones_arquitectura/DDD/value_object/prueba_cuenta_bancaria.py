from DDD.value_object.cuenta_bancaria import *

mi_dinero = Dinero(100, Moneda.Pesos)
print(mi_dinero.moneda)
print(mi_dinero.monto)

mi_cuenta = CuentaBancaria(1, mi_dinero)

print(mi_cuenta.balance.monto)
print(mi_cuenta.balance.moneda)