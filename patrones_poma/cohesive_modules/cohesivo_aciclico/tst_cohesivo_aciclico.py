from POMA.cohesive_modules.cohesivo_aciclico.factura.factura import *
from POMA.cohesive_modules.cohesivo_aciclico.ruteador.ruteador_tipoA import *

mi_factura = Factura("A", "1", 200.20, RuteadorTipoA())

print(mi_factura.rutear())
print(mi_factura.obtener_prioridad())
