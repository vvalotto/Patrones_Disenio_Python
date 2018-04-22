from Command.command_unix.command_unix import *
from Command.command_unix.invocador import *

#Cliente

ls_receptor = LsReceptor()
ls_command = LsCommand(ls_receptor)

touch_receptor = TouchReceptor('test_file')
touch_command = TouchCommand(touch_receptor)

rm_receptor = RmReceptor('test_file')
rm_command = RmCommand(rm_receptor)

commandos_crear_archivo = [ls_command, touch_command, ls_command]
commandos_borrar_archivo = []

invocador = Invocador(commandos_crear_archivo, commandos_borrar_archivo)

invocador.crear_archivo()
#invocador.borrar_archivo()
invocador.dehacer()