
class ModeloDefecto:
    def __init__(self, conn):
        self._conn = conn

    def get_lista(self,componente):
        query = ''' select * from defectos where componente = '%s' ''' %componente
        lista_defectos = self._dbselect(query)
        lista = []
        for fila in lista_defectos:
            lista.append(fila[1])
        lista_defectos.close()
        return lista

    def get_sumario(self,id):
        query = ''' select sumario from defectos where defectos_ID = '%d' ''' %id
        sumario = self._dbselect(query)
        for fila in sumario:
            return fila[0]
        sumario.close()

    def _dbselect(self, query):
        cursor_obj = self._conn.cursor()
        return cursor_obj.execute(query)
