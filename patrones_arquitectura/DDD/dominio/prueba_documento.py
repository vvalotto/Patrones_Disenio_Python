from DDD.dominio.documento import *
from DDD.dominio.cliente import *

a = 14367839
mi_documento = Documento("CUIT", a)
print(mi_documento)

cliente = Cliente()
cliente.asignar_documento(mi_documento)
print(cliente.id)
print(cliente.documento)
