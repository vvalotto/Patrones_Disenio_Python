
from POMA.manage_relationship.separacion.cliente.cliente import *
from POMA.manage_relationship.separacion.factura.factura_comun import *

uncliente = Cliente()
uncliente.agregar_factura(FacturaComun(uncliente,(500)))
uncliente.agregar_factura(FacturaComun(uncliente,(700)))

for f in uncliente.facturas:
    print(f.cantidad)

print(uncliente.obtener_descuento())