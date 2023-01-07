from django.test import TestCase
from aluraflix.models import Programa

class FixtureDataTestCase(TestCase):
    fixtures = ['programas_iniciais']

    def test_verify_fixture_load(self):
        total_number_programs = 9
        program_id = 1

        programa_bizarro = Programa.objects.get(pk=program_id)
        all_programs = Programa.objects.all()

        self.assertEqual(programa_bizarro.titulo, 'Coisas bizarras')
        self.assertEqual(len(all_programs), total_number_programs)
