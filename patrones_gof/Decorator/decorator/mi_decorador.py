import time

def log_errores(funcion):

    def logging(*args):

        try:
           return funcion(*args)
        except Exception as ex:
            print("Error:", ex)
    return logging

def log_ingresa_funcion(funcion):

    def log_ingresar(*args):
        print("Funcion:", funcion.__name__)
        return funcion(*args)
    return log_ingresar

def log_temporizar(funcion):

    def temporizar(*args):
        marca_tiempo = time.time()
        valor_retorno = funcion(*args)
        print("Duración: {0}".format(time.time() - marca_tiempo))
        return valor_retorno
    return temporizar