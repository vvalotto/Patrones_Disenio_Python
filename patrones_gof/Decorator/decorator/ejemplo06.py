"""
decorador 01
"""

def obtener_texto(nombre):
    return "Como estas {0}?. Todo bien".format(nombre)

def p_decorador(func):

    def func_envolver(nombre):
        return "<p>{0}</p>".format(func(nombre))

    return func_envolver

mi_funcion = p_decorador(obtener_texto)

print(mi_funcion("Alejo"))