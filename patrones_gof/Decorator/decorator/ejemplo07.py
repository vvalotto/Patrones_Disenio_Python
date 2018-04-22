"""
Python decorator
"""


def p_decorador(func):
    def func_envolver(nombre):
        return "<p>{0}</p>".format(func(nombre))
    return func_envolver



@p_decorador
def obtener_texto(nombre):
    return "Como estas {0}?. Todo bien".format(nombre)




print(obtener_texto("Alejo"))