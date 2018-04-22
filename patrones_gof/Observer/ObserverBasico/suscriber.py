class Subscriber(object):
    def __init__(self):
    # make it uninheritable
        pass

    def notificar(self):
    #sobreescribir
        pass

class Usuario1(Subscriber):
    def notify(self, postname):
        print('User1 notfied of a new post %s' % postname)

class Usuario2(Subscriber):
    def notify(self, postname):
        print('User1 notfied of a new post %s' % postname)

class SisterSites(Subscriber):
    def __init__(self):
        self._sisterWebsites = ["Site1", "Site2", "Site3"]

    def notify(self, postname):
        for site in self._sisterWebsites:
            # Send updates by any means
            print( "Sent nofication to site: %s" % site)

