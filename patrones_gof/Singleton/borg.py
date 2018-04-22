class Borg(object):
    _estado_compartido = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg,cls).__new__(cls, *arg, **kwargs)
        obj.__dict__ = cls._estado_compartido
        return obj