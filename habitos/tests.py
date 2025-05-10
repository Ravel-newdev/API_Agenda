from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Habito

# Create your tests here.

class Teste_funcionamento_agenda(APITestCase):
    def setUp(self):
        self.url = '/agenda/'
        self.habito_data = {
            'nome': 'Estudar Redes',
            'frequencia': 'diario',
            'desc': 'Não entendi oque o professor falou',
            'status': 'ativo'
        }

    def test_criar_habito(self):
        response = self.client.post(self.url, self.habito_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], self.habito_data['nome'])
        self.assertEqual(response.data['desc'], self.habito_data['desc'])

    def test_listar_habitos(self):
        self.client.post(self.url, self.habito_data, format='json')
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_deletar_habito(self):
        post_response = self.client.post(self.url, self.habito_data, format='json')
        habito_id = post_response.data['id']
        delete_response = self.client.delete(f'{self.url}{habito_id}/', format='json')
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        get_response = self.client.get(self.url, format='json')
        self.assertEqual(len(get_response.data), 0)
