from POMA.cohesive_modules.cohesivo_ciclico.factura.factura import *
from POMA.cohesive_modules.cohesivo_ciclico.ruteador.ruteador_tipoA import *

mi_factura = Factura("A", "1", 200.20, RuteadorTipoA())

print(mi_factura.ruteador)