import sqlite3

class AccesoDatos():
    def __init__(self, bd):
        self._bd = bd

    def conectar(self):
        self._conn = sqlite3.connect(self._bd)
        return self._conn

    def cerrar(self):
        self._conn.close()