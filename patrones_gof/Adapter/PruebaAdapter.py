"""
Patron Adapter

Prueba del Ejemplo
"""

from Adapter.pato_adaptado import *
from Adapter.pavo_adaptado import *


def ProbarPato(pato_base):
    '''
    Tipo Cliente que usa la interfaz de los tipos de pato
    '''
    pato_base.volar()
    pato_base.graznar()

def ProbarPavo(pavo_base):
    '''
    Tipo Cliente que usa la interfaz de los tipos de pavo
    '''
    pavo_base.volar()
    pavo_base.guglutear()


if __name__ == '__main__':
    '''
    Programa que muestra el uso del patrón
    '''
    pato = PatoCriollo()                     # Pato Real
    pavo = PavoSilvestre()                   # Pavo Real
    pavo_tipo_pato = PavoAdaptado(pavo)      # Pavo que parece un pato
    pato_tipo_pavo = PatoAdaptado(pato)      # Pato que parece un pavo

    ProbarPavo(pavo)
    ProbarPato(pato)
    ProbarPato(pavo_tipo_pato)               # Pavo que se usa como pato (El cliente lo ve como pato)
    ProbarPavo(pato_tipo_pavo)               # Pato que se usa como pavo (El cliente lo ve como pavo)







