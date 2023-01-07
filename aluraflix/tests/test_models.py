from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):
    TITLE = 'Procurando Ninguém'
    DATE = '2005-06-10'

    def setUp(self):
        self.programa = Programa(
            titulo = self.TITLE,
            data_lancamento = self.DATE
        )

    def test_verify_attributes_default(self):
        self.assertEqual(self.programa.titulo, self.TITLE)
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.data_lancamento, self.DATE)
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)

