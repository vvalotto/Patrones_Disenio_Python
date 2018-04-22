from unittest import TestCase
from DDD.entidades.libro import *

class TestLibro(TestCase):

    def setUp(self):
        self._ISBN = ISBN('1234567890')
        self._mi_libro = Libro(self._ISBN)

    def test_id(self):
        self.assertEqual(self._mi_libro.id, '1234567890')

    def test_isbn(self):
        self.assertEqual(self._mi_libro.isbn.numero, '1234567890')

