from Observer.ObserverBasico import suscriber, publisher

if __name__ == "__main__":

    usuario1 = suscriber.Usuario1()
    usuario2 = suscriber.Usuario2()
    sites = suscriber.SisterSites()

    pub = publisher.TechForum()

    pub.registrar(usuario1)
    pub.registrar(usuario2)

    pub.writeNewPost("Patron Observer")

    pub.deregistrar(usuario2)

    pub.writeNewPost("Patron MVC")