class Cliente:
    def __init__(self, nombre, direccion, telefono, email):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def obtener_direccion(self):
        return self.direccion

class VerificadorDireccion:
    def verificar(self, cliente):
        direccion = cliente.obtener_direccion()
        # Lógica para verificar la dirección
        return True if direccion else False

cliente = Cliente("Maria", "Calle Falsa 123", "123456789", "maria@example.com")
verificador = VerificadorDireccion()
es_valida = verificador.verificar(cliente)
print(f"La dirección de {cliente.nombre} es válida: {es_valida}")
