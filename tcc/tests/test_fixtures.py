from django.test import TestCase
from tcc.models import Register, Create

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_loading_of_fixtures(self):
        """Test that verifies fixture loading"""
        register = Register.objects.get(cell='34 94465-7331')  
        create = Create.objects.get(pk=1)
        
        self.assertEqual(register.cell, "34 94465-7331")  
        self.assertEqual(create.task, "CPOO1")  
