from abc import ABCMeta, abstractmethod

import os

historia = []

class Command(metaclass=ABCMeta):
    """La Interfase Command"""

    @abstractmethod
    def ejecutar(self):
        """Metodo para ejecutar el commnad"""
        pass

    @abstractmethod
    def deshacer(self):
        """Metodo para deshacer el command"""
        pass


class LsCommand(Command):

    def __init__(self, receptor):
        self.receptor = receptor

    def ejecutar(self):
        self.receptor.mostrar_dir_actual()

    def deshacer(self):
        pass


class LsReceptor(object):

    def mostrar_dir_actual(self):
        dir_actual = './'
        nombre_archivos = []
        for narchivo in os.listdir(dir_actual):
            if os.path.isfile(os.path.join(dir_actual, narchivo)):
                nombre_archivos.append(narchivo)
        print('Contenido, de dir: ', os.path.join(nombre_archivos))


class TouchCommand(Command):

    def __init__(self, receptor):
        self.receptor = receptor

    def ejecutar(self):
        self.receptor.crear_archivo()

    def deshacer(self):
        self.receptor.borrar_archivo()

class TouchReceptor(object):

    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def crear_archivo(self):
        with open (self.nombre_archivo, 'a'):
            os.utime(self.nombre_archivo, None)

    def borrar_archivo(self):
        os.remove(self.nombre_archivo)


class RmCommand(Command):

    def __init__(self, receptor):
        self.receptor = receptor

    def ejecutar(self):
        self.receptor.borrar_archivo()

    def deshacer(self):
        self.receptor.deshacer()

class RmReceptor(object):

    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.nombre_back_up = None


    def borrar_archivo(self):
        self.nombre_back_up = './' + self.nombre_archivo
        os.rename(self.nombre_archivo, self.nombre_back_up)

    def deshacer(self):
        nombre_original = self.nombre_back_up[1:]
        os.rename(self.nombre_back_up, nombre_original)
        self.nombre_back_up = None





