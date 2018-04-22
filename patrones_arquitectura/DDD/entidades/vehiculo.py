"""
Metodo Factory estático
"""

class Vehiculo:

    @property
    def id(self):
        return self._id

    def __init__(self, id):
        self._id = id
        return