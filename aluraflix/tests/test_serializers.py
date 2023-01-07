from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):
    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando Ninguém',
            data_lancamento = '2005-06-10',
            tipo = 'F',
            likes = 230,
            dislikes = 37,
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verify_serializer_field(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))

    def test_verify_serializer_content_field(self):
        data = self.serializer.data

        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['likes'], self.programa.likes)
        # self.assertEqual(data['dislikes'], self.programa.dislikes)
