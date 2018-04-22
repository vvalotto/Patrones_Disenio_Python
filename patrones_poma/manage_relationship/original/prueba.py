from POMA.manage_relationship.original.cliente.cliente import *
from POMA.manage_relationship.original.factura.factura import *

uncliente = Cliente()
uncliente.crear_factura(uncliente, 100)
uncliente.crear_factura(uncliente, 200)

for f in uncliente.facturas:
    print(f.cantidad)

print(uncliente.obtener_descuento())