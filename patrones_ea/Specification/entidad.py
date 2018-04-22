from Specification.ispecification import *

class Usuario:

    @property
    def nombre(self):
        return self._nombre

    @property
    def empresa(self):
        return self._empresa

    @property
    def ciudad(self):
        return self._ciudad

    def __init__(self, nombre, empresa, ciudad):
        self._nombre = nombre
        self._empresa = empresa
        self._ciudad = ciudad


class EspecificacionUsuario(BaseEspecificacion):

    def es_satisfecho_por(self, usuario):
        return True

class RepositorioUsuario:

    def __init__(self):
        return

    def obtener_por_especificacion(self, especicacion):
        lista_selececcionada = []
        lista_total_usuarios = self._obtener_usuarios()
        for usuario in lista_total_usuarios:
            if (especicacion.es_satisfecho_por(usuario)):
                lista_selececcionada.append(usuario)

        return lista_selececcionada

    def _obtener_usuarios(self):

        lista = []
        lista.append(Usuario('a','A1', 'Parana'))
        lista.append(Usuario('b', 'A2', 'Santa Fe'))
        lista.append(Usuario('c', 'A1', 'Santa Fe'))

        return lista

class EspecificacionUsuarioEmpresa(EspecificacionUsuario):

    def __init__(self, empresa):
        self._empresa = empresa

    def es_satisfecho_por(self, usuario):
        return usuario.empresa == self._empresa

class EspecificacionUsuarioCuidad(EspecificacionUsuario):

    def __init__(self, cuidad):
        self._ciudad = cuidad

    def es_satisfecho_por(self, usuario):
        return usuario.ciudad == self._ciudad

if __name__ == '__main__':
    mi_repo = RepositorioUsuario()
    usuario_por_empresa = EspecificacionUsuarioEmpresa('A1')
    usuario_por_cuidad = EspecificacionUsuarioCuidad('Parana')
    lista = mi_repo.obtener_por_especificacion(usuario_por_empresa)
    for usuario in lista:
        print(usuario.nombre)
    lista = mi_repo.obtener_por_especificacion(usuario_por_cuidad)
    for usuario in lista:
        print(usuario.nombre)