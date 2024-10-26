from rest_framework import serializers
from tcc.models import Register,Create

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['name', 'email' , 'cpf', 'date_of_birth', 'cell']
        
class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Create
        fields = '__all__'