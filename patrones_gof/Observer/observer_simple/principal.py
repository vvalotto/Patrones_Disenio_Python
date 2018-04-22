from Observer.observer_simple.subject import *
from Observer.observer_simple.observador import *

subject = Subject()

print('Agregando observador del tiempo USA')
observador1 = ObservadorTiempoUSA('obs_tiempo_USA')
subject.registrar_observador(observador1)
subject.notificar_observadores()

time.sleep(2)
print('Agregando observador del tiempo EU')
observador2 = ObservadorTiempoEUT('obs_tiempo_EU')
subject.registrar_observador(observador2)
subject.notificar_observadores()

time.sleep(2)
print('Sacando observador del timepo USA')
subject.sacar_observador(observador1)
subject.notificar_observadores()
