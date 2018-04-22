
class Invocador(object):

    def __init__(self, comandos_crear_archivo, comandos_borrar_archivos):
        self.comandos_crear_archivos = comandos_crear_archivo
        self.comandos_borrar_archivos = comandos_borrar_archivos
        self.historia = []

    def crear_archivo(self):
        print('Creando archivo')

        for comando in self.comandos_crear_archivos:
            comando.ejecutar()
            self.historia.append(comando)

        print('Archivo creado')


    def borrar_archivo(self):

        print('Borrando archivo')

        for comando in self.comandos_borrar_archivos:
            comando.ejecutar()
            self.historia.append(comando)

        print('Archivo borrado')

    def dehacer(self):

        print('Deschacer todo')

        for comando in reversed(self.historia):
            comando.deshacer()

        print('Deshacer todo finalizado')

