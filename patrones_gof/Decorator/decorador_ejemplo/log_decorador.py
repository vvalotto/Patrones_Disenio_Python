
class LogSocket(object):

    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print("Enviando {0} a {1}".format(data, self.socket.getpeername()[0]))
        self.socket.send(data)

    def close(self):
        self.socket.close()

