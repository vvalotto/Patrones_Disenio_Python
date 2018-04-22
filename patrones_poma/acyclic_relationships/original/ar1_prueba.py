from POMA.acyclic_relationships.original.cliente.cliente import *
from POMA.acyclic_relationships.original.factura.factura import *

uncliente = Cliente()
uncliente.crear_factura(uncliente, 100)
uncliente.crear_factura(uncliente, 200)

for f in uncliente.facturas:
    print(f.cantidad)

print(uncliente.obtener_descuento())