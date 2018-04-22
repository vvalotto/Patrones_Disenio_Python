import socket

from Decorator.decorador_ejemplo.log_decorador import LogSocket


def responder(cliente):
    respuesta = input('Ingresar un valor')
    cliente.send(bytes(respuesta, 'utf8'))
    cliente.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2401))
server.listen(1)
try:
    while True:
        cliente, addr = server.accept()
        responder(LogSocket(cliente))
finally:
    server.close()

