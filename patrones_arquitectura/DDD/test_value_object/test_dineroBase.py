import unittest
from DDD.value_object.dinero import *


class TestDineroBase(unittest.TestCase):

    def setUp(self):
        self._mi_dinero = Dinero()

    def test_monto(self):
       self.assertEqual(self._mi_dinero.monto, 0, 'Bien')

    def test_moneda(self):
        self.assertEqual(self._mi_dinero.moneda, Moneda.Pesos, 'Bien')

    def test_sumar(self):
        otro_dinero = Dinero(55)
        self.assertEqual(self._mi_dinero.sumar(otro_dinero).monto, 55, 'Bien')

    def test_restar(self):
        otro_dinero = Dinero(55)
        self.assertEqual(self._mi_dinero.restar(otro_dinero).monto, -55, 'Bien')

    def test_obtener_atributos_incluidos_en_chequeo_igualdad(self):
        self.assertEqual(self._mi_dinero.obtener_atributos_incluidos_en_chequeo_igualdad(),
                         [0, Moneda.Pesos])


if __name__ == '__main__':
    unittest.main()