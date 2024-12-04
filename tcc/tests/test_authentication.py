from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status



class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Register-list') 

    def test_user_authentication_with_correct_credentials(self):
        """Test that verifies the authentication of a user with the correct credentials"""
        user = authenticate(username='admin', password='admin')
        self.assertIsNotNone(user)  
        self.assertTrue(user.is_authenticated) 
    def test_authentication_user_with_incorrect_username(self):
        """Test that verifies authentication with incorrect username"""
        user = authenticate(username='admn', password='admin')
        self.assertIsNone(user) 
    def test_autenticacao_user_com_senha_incorreta(self):
        """Teste que verifica a autenticação com senha incorreta"""
        usuario = authenticate(username='admin', password='adm')
        self.assertIsNone(usuario) 

    def test_authorized_get_request(self):
        """Test that verifies an authorized GET request"""
        self.client.force_authenticate(user=self.user) 
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  

    def test_request_get_not_authorized(self):
        """Test that checks for an unauthorized GET request"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  
