
class VistaDefecto:
    def mostrar_resumen(self, resumen, id_defecto):
        print("#### Resumen del Defecto para el defecto# %d####\n%s" % (id_defecto, resumen))

    def mostrar_lista_defectos(self, lista, categoria):
        print ("#### Defect List for %s ####\n" % categoria)
        for defecto in lista:
            print(defecto)