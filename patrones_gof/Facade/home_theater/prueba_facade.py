"""
Patron Facade
Prueba
"""
from Facade.amplificador import *
from Facade.home_theater_facade import *
from Facade.luces import *
from Facade.pantalla import *
from Facade.proyector import *
from Facade.reproductor_CD import *
from Facade.sintonizador import *

from Facade.home_theater.reproductor_DVD import *


class PruebaFacade:

    def probar(self):

        amp = Amplificador("AMPLIFIER")
        sin = Sintonizador("TUNER", amp)
        dvd = ReproductorDVD("DVD PLAYER", amp)
        cd = ReproductorCD("CD PLAYER", amp)
        proy = Proyector("PROYECTOR", dvd)
        luz = Luces("LIGHTS")
        pant = Pantalla("SCREEN")

        mi_home_theater = HomeTheaterFacade(amp, sin, dvd, cd,
                                            luz, pant, proy)
        mi_home_theater.mirar_pelicula("Mad Max")
        mi_home_theater.terminar_pelicula()
        return

if __name__ == "__main__":

    PruebaFacade().probar()
