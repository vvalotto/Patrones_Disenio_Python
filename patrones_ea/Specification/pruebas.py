from Specification.dominio import *

si = True
no = False
domicilio_envio = Domicilio()
domicilio_envio.direccion = 'Corrientes 659'
domicilio_envio.ciudad = 'Parana'
domicilio_envio.estado = 'ER'
domicilio_envio.pais = 'ARG'

producto_A = Producto(si, si)
producto_A.precio = 25
producto_B = Producto(no, no)
producto_B.precio = 15
producto_C = Producto(si, si)
producto_C.precio = 20

pedido = Pedido()
pedido.direccion_destino = domicilio_envio
#pedido.agregar_item(producto_A)
pedido.agregar_item(producto_B)
pedido.agregar_item(producto_C)

items = pedido.obtener_items_pedido()
for item in items:
    print(item.precio)

if pedido.es_rapido():
    print('Pedido rapido')
else:
    print('Pedido normal')
