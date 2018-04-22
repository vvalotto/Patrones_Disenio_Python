from MVC.Controlador.controlador import *
from MVC.Modelo.acceso_datos import *

controlador = Controlador()

print(controlador.get_resumen_defecto(2))

print(controlador.get_lista_defectos('XYZ'))
