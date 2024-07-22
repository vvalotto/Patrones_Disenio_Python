class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def obtener_horas_trabajadas(self):
        return self.horas_trabajadas

    def obtener_tarifa_por_hora(self):
        return self.tarifa_por_hora

class CalculadoraSalario:
    def calcular_salario(self, horas_trabajadas, tarifa_por_hora):
        return horas_trabajadas * tarifa_por_hora

empleado = Empleado("Juan", 40, 20)
calculadora = CalculadoraSalario()
salario = calculadora.calcular_salario(empleado.obtener_horas_trabajadas(),
                                       empleado.obtener_tarifa_por_hora())
print(f"El salario de {empleado.nombre} es: {salario}")
