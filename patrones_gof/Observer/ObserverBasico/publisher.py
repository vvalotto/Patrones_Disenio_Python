class Publisher(object):
    def __init__(self):
        #No es heredado
        pass

    def registar(self):
        #sobreescrito
        pass

    def deregistrar(self):
        #sobreescrito
        pass

    def notificar_todos(self):
        #sobreescrito
        pass

class TechForum(Publisher):
    def __init__(self):
        self._lista_de_usuarios = []
        self.postnema = None

    def registrar(self, usuario):
        if usuario not in self._lista_de_usuarios:
            self._lista_de_usuarios.append(usuario)

    def deregistrar(self, usuario):
        self._lista_de_usuarios.remove(usuario)

    def notificar_todos(self):
        for objects in self._lista_de_usuarios:
            objects.notify(self.postname)

    def writeNewPost(self, postname):
        # User writes a post.
        self.postname = postname
        # When submits the post is published and notification is sent to all
        self.notificar_todos()