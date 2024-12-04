from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from tcc.models import Register
from tcc.serializers import RegisterSerializer

class RegistersTestCase(APITestCase):
    fixtures = ['prototype_bank.json']

    def setUp(self):
        
        self.usuario = User.objects.get(username='agle') 
        self.url = reverse('Registers-list')  
        self.client.force_authenticate(user=self.usuario) 

        
        self.register_01 = Register.objects.get(pk=1)
        self.register_02 = Register.objects.get(pk=2)
        
    def test_request_get_to_list_registers(self):
        """Testa requisição GET para listar todos os registros"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_request_get_to_list_a_registers(self):
        """Testa requisição GET para um registro específico"""
        url = reverse('Registers-detail', args=[1])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_register = Register.objects.get(pk=1)
        data_register_serialized = RegisterSerializer(instance=data_register).data
        self.assertEqual(response.data, data_register_serialized)
        
    def test_request_post_to_create_a_register(self):
        """Testa requisição POST para criar um novo registro"""
        data = {
            'name': 'teste',
            'email': 'teste@gmail.com',
            'date_of_birth': '2003-05-04',
            'cell': '11 99999-9999'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_a_register(self):
        """Testa requisição DELETE para excluir um registro"""
        response = self.client.delete(reverse('Registers-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_request_to_update_a_register(self):
        """Testa requisição PUT para atualizar um registro"""
        data = {
            'name': 'teste',
            'email': 'testeput@gmail.com',
            'date_of_birth': '2003-05-09',
            'cell': '11 88888-6666'
        }
        response = self.client.put(reverse('Registers-detail', args=[1]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
