from Specification.especificaciones import *


class Producto:

    @property
    def hay_stock(self):
        return self._hay_stock

    @hay_stock.setter
    def hay_stock(self, valor):
        self._hay_stock = valor
        return

    @property
    def tiene_material_peligroso(self):
        return self._tiene_material_peligroso

    @tiene_material_peligroso.setter
    def tiene_material_peligroso(self, valor):
        self._tiene_material_peligroso = valor
        return

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor
        return

    def __init__(self, hay_stock, tiene_material_peligroso):
        self._hay_stock = hay_stock
        self._tiene_material_peligroso = tiene_material_peligroso
        self._precio = 0


class Domicilio:

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, valor):
        self._direccion = valor
        return

    @property
    def ciudad(self):
        return self._ciudad

    @ciudad.setter
    def ciudad(self, valor):
        self._ciudad = valor
        return

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor
        return

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, valor):
        self._pais = valor
        return

    def __init__(self):
        self._direccion = None
        self._ciudad = None
        self._estado = None
        self._pais = None


class Pedido:

    @property
    def direccion_destino(self):
        return self._direccion_destino

    @direccion_destino.setter
    def direccion_destino(self, valor):
        self._direccion_destino = valor
        return

    @property
    def pedido_total(self):
        return self._pedido_total

    def __init__(self):
        self._items_pedido = []
        self._direccion_destino = None
        self._pedido_total = 0
        return

    def agregar_item(self, item):
        self._items_pedido.append(item)
        self._pedido_total += item.precio
        return

    def obtener_items_pedido(self):
        return self._items_pedido

    def es_rapido(self):
        especificacion = PedidoRapidoEspecificacion()
        return especificacion.es_satisfecho_por(self)
