from .framework import *


class PedidoDomesticoEspecificacion(BaseEspecificacion):
    """
    Define la especificacion que el pedido
    debe ser local
    """
    def es_satisfecho_por(self, pedido):
        return pedido.direccion_destino.pais == 'ARG'


class MaterialPeligrosoEspecificacion(BaseEspecificacion):
    '''
    Define la especificacion para evaluar si tiene material
    peligroso
    '''

    def es_satisfecho_por(self, pedido):
        items = pedido.obtener_items_pedido()
        hay_peligro = 0
        for i in items:
            if i.tiene_material_peligroso:
                hay_peligro += 1
        return hay_peligro > 0


class PedidoValorElevadoEspecificacion(BaseEspecificacion):
    '''
    Evalua si el pedido tiene un valor alto
    '''

    def es_satisfecho_por(self, pedido):
        items = pedido.obtener_items_pedido()
        valor_pedido = 0
        for i in items:
            valor_pedido += i.precio
        return valor_pedido > 20

class HayStockEspecificacion(BaseEspecificacion):
    '''
    Evalua si hay stock para el pedido
    '''
    def es_satisfecho_por(self, pedido):
        items = pedido.obtener_items_pedido()
        hay_stock = True
        for i in items:
            if not i.hay_stock:
                hay_stock = False
        return hay_stock

class PedidoRapidoEspecificacion(BaseEspecificacion):
    '''
    Evalua se en un pedido de salida rapida
    '''
    def __init__(self):
        self._pedido_local_espec = PedidoDomesticoEspecificacion()
        self._valor_alto_espec = PedidoValorElevadoEspecificacion()
        self._material_peligroso_espec = MaterialPeligrosoEspecificacion()
        self._hay_stock_espec = HayStockEspecificacion()

    def es_satisfecho_por(self, candidata):
        return self._pedido_local_espec\
            .y(self._material_peligroso_espec)\
            .y(self._hay_stock_espec)\
            .y(self._valor_alto_espec)\
            .es_satisfecho_por(candidata)
