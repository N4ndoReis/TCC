from django.test import TestCase
from tcc.models import Register
from tcc.serializers import RegisterSerializer

class SerializerRegisterTestCase(TestCase):
    def setUp(self):
        self.register = Register(
            name = 'Model Test',
            email = 'testedemodelo@gmail.com',
            date_of_birth = '2023-02-02',
            cell = '86 99999-9999'
        )
        self.serializer_register = RegisterSerializer(isinstance=self.register)
            
    def checks_serialized_record_fields(self):
        """Test that checks the fields being serialized from register"""
        data = self.serializer_register.data
        self.assertEqual(set(data.keys()),set([all]))
    def test_checks_content_of_student_serialized_fields(self):
        """Test that verifies the contents of the fields being serialized from register"""
        data = self.serializer_register.data
        self.assertEqual(data['name'],self.register.name)
        self.assertEqual(data['email'],self.register.email)
        self.assertEqual(data['date_of_birth'],self.register.date_of_birth)
        self.assertEqual(data['cell'],self.register.cell)
        
        