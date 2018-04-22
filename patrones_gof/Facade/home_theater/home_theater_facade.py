"""
Tipo Facade
Controla y tiene un interfaz mas simple que cada uno de los dispositivos
"""

class HomeTheaterFacade:

    def __init__(self, amplificador,
                 sintonizador,
                 reproductor_dvd,
                 reproductor_cd,
                 luces,
                 pantalla,
                 proyector):

        self._sintonizador = sintonizador
        self._amplificador = amplificador
        self._reproductor_dvd = reproductor_dvd
        self._reproductor_cd = reproductor_cd
        self._luces = luces
        self._pantalla = pantalla
        self._proyector = proyector
        return

    def mirar_pelicula(self, pelicula):

        print('La pelicula está por empezar..')
        self._luces.atenuar(10)
        self._pantalla.abrir()
        self._proyector.on()
        self._proyector.poner_modo_widescreen()
        self._amplificador.on()
        self._amplificador.poner_dvd(self._reproductor_dvd)
        self._amplificador.poner_surround()
        self._amplificador.poner_volumen(5)
        self._reproductor_dvd.on()
        self._reproductor_dvd.reproducir(pelicula)
        return

    def terminar_pelicula(self):

        print('Apangando la pelicula del HomeTheater')
        self._luces.off()
        self._pantalla.cerrar()
        self._proyector.off()
        self._amplificador.off()
        self._reproductor_dvd.parar()
        self._reproductor_dvd.expulsar()
        self._reproductor_dvd.off()
        return

    def escuchar_cd(self, titulo_cd):

        return

    def terminar_cd(self):

        return

    def escuchar_radio(self):

        return

    def terminar_radio(self):

        return