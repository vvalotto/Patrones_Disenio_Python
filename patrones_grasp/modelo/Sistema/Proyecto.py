#######################################################
# 
# Proyecto.py
# Python implementation of the Class Proyecto
# Generated by Enterprise Architect
# Created on:      14-sep-2013 11:50:32 a.m.
# 
#######################################################

from datetime import date,time

class proyecto:

    def __init__(self, nombre = 'Sin Nombre'):
        self._nombre = nombre
        return

    ''' Nombre'''
    def _get_nombre(self):
        return self._nombre

    def _set_nombre(self, valor):
        self._nombre = valor
        return
    
    '''Fecha Inicio'''
    def _get_fecha_inicio(self):
        return self._fecha_inicio

    def _set_fecha_inicio(self, valor):
        self._fecha_inicio = valor
        return
    
    nombre = property(_get_nombre, _set_nombre)
    fecha_inicio = property(_get_fecha_inicio, _set_fecha_inicio)
    
    def duracion_dias(self):
        return date.today() - self._fecha_inicio
    
    
    def duracion_anios(self):
        return (self.duracion_dias() / 365)
    
    def duracion_meses(self):
        return (self.duracion_anios() * 12)
    
    
    
    
    
    
    