from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from tcc.models import Register
from tcc.serializers import RegisterSerializer

class RegistersTestCase(APITestCase):
    fixtures = ['prototype_bank.json']
    def setUp(self):
        #self.user = User.objects.create_superuser(username='admin',password='admin')
        self.usuario = User.objects.get(username='agle')
        self.url = reverse('Registers-list')
        self.client.force_authenticate(user=self.user)
        
        self.register_01 = Register.objects.get(pk=1)
        self.register_02 = Register.objects.get(pk=2)
        
    def test_request_get_to_list_registers(self):
        """GET request test"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_request_get_to_list_a_registers(self):
        """Testing a GET request for a register"""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        data_register = Register.objects.get(pk=1)
        data_register_serialized = RegisterSerializer(instance=data_register).data
        self.assertEqual(response.data,data_register_serialized)
        
    def test_request_post_to_create_a_register(self):
        """Testing a POST request for a register"""
        data = {
            'name':'teste',
            'email':'teste@gmail.com',
            'date_of_birth':'2003-05-04',
            'cell':'11 99999-9999'
        }
        response = self.client.post(self.url,data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_request_delete_a_register(self):
        """Test request DELETE a register"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_put_request_to_update_a_register(self):
        """PUT request test for a register"""
        data = {
            'name':'teste',
            'email':'testeput@gmail.com',
            'date_of_birth':'2003-05-09',
            'cell':'11 88888-6666'
        }
        response = self.client.put(f'{self.url}1/',data=data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)