"""

"""

from Command.hf_simple_remote.control_remoto import *
from Command.hf_simple_remote.luz import *
from Command.hf_simple_remote.garage import *
from Command.hf_simple_remote.command import *

control_remoto = ControlRomotoSimple()
luz = Luz()
prender = ComandoPrenderLuz(luz)
garage = Garage()
abrir = ComandoAbrirGarage(garage)

control_remoto.slot = prender
control_remoto.presionar_boton()

control_remoto.slot = abrir
control_remoto.presionar_boton()


