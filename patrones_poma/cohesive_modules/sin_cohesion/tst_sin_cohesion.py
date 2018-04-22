from POMA.cohesive_modules.sin_cohesion.facturas.factura import *
from POMA.cohesive_modules.sin_cohesion.facturas.ruteador_tipoA import *

mi_factura = Factura("A", "1", 200.20, RuteadorTipoA())

print(mi_factura.ruteador)