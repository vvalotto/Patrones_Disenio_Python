from POMA.acyclic_relationships.escalado.cliente.cliente import *
from POMA.acyclic_relationships.escalado.mediador.mediador_pago import *

uncliente = Cliente()
mediador = MediadorPago(uncliente)
uncliente.crear_factura(100)
uncliente.crear_factura(200)

for f in uncliente.facturas:
    print(f.cantidad)
    print(mediador.pagar(f))

