"""
Ejemplo de uso del patron Observer
Programa principal
"""

from Observer.hf_estacion_clima.datos_clima import *
from Observer.hf_estacion_clima.visualizadores import *

# Se crea la instancia de la estación de medición
estacion_datos_clima = DatosClima()
# Se crea un visualizador de condiciones climaticas y se suscribe a la estación
condiciones_actuales = VisualizadorCondicionesActuales(estacion_datos_clima)
pronostico = VisualizadorPronostico(estacion_datos_clima)
estadisticas = VisualizadorEstadisticas(estacion_datos_clima)
indice_calor = VisualizadorIndiceCalor(estacion_datos_clima)


# La estación de clima actualiza los datos del clima
print("")
estacion_datos_clima.poner_mediciones(20, 85, 1013)
print("")
estacion_datos_clima.poner_mediciones(21, 87, 1015)
print("")
estacion_datos_clima.poner_mediciones(24, 89, 1014)



