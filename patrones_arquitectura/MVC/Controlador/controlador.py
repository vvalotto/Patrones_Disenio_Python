
from MVC.Modelo.modelo_defecto import *
from MVC.Modelo.acceso_datos import *
from MVC.Vista.vista_defecto import *

class Controlador:
    def __init__(self):
        self._conn = AccesoDatos('TMS.db').conectar()
        pass

    def get_resumen_defecto(self, id_defecto):
        modelo = ModeloDefecto(self._conn)
        vista = VistaDefecto()
        resumen = modelo.get_sumario(id_defecto)
        return vista.mostrar_resumen(resumen, id_defecto)

    def get_lista_defectos(self, componente):
        modelo = ModeloDefecto(self._conn)
        vista = VistaDefecto()
        lista_defectos = modelo.get_lista(componente)
        return vista.mostrar_lista_defectos(lista_defectos, componente)