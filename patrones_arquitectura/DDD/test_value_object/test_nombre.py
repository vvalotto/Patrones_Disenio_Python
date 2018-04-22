import unittest
from DDD.value_object.tipos_ov import *


class test_nombre(unittest.TestCase):
    def test_nombre(self):
        mi_nombre = Nombre('victor', 'valotto')
        self.assertEqual(mi_nombre.nombre, 'Victor')
        self.assertEqual(mi_nombre.apellido, 'Valotto')

if __name__ == '__main__':
    unittest.main()
