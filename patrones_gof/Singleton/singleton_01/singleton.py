class SoloUna:

    instancia = None

    class __SoloUna:
        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return self.val

    def __init__(self, arg):
        if not SoloUna.instancia:
            SoloUna.instancia = SoloUna.__SoloUna(arg)
        else:
            SoloUna.instancia.val = arg

    def __getattr__(self, nombre):
        return getattr(self.instancia, nombre)

