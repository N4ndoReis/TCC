from django.test import TestCase
from tcc.models import Register
from datetime import date

class ModelRegisterTestCase(TestCase):

    def setUp(self):
        self.register = Register.objects.create(
            name='Model Test',
            email='testedemodelo@gmail.com',
            date_of_birth=date(2023, 2, 2),
            cell='86 99999-9999'
        )

    def test_check_attributes_register(self):
        """Test that checks the attributes of the register model"""
        self.assertEqual(self.register.name, 'Model Test')
        self.assertEqual(self.register.email, 'testedemodelo@gmail.com')
        self.assertEqual(self.register.date_of_birth, date(2023, 2, 2))  
        self.assertEqual(self.register.cell, '86 99999-9999')
