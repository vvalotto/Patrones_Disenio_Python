'''
Created on 25/11/2013

@author: voval
'''
from senial import *
from repositorio_senial import *
from lector_valor_senial import *
from adquisidor_senial import *
from procesador_senial import *

s = SenialSimple()
r = RepositorioSenialArchivo()
p = RepositorioSenialPickle()
l = LectorPrueba()
s.inicializar()

adq = AdquisidorSenial(s,l)

print('Inicio')
adq.leer_senial()

print('Senial lieda')
r.guardar_senial(s)
p.guardar_senial(s)

print('Senial Guardada')
adq.mostrar_señal()
print(r.obtener_senial())

s2 = SenialSimple()
s2.inicializar()
s2.volcar(r.obtener_senial())

s3 = SenialSimple()
s3.inicializar()
s3 = p.obtener_senial()
print("Pickle >")
print(s3._valores, s3._tamanio)
print(s2._valores)

p1 = ProcesadorMax()
print(p1.procesar_señal(s2._valores))


if __name__ == '__main__':
    pass