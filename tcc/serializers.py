from rest_framework import serializers
from tcc.models import Register,Login,Create

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['name', 'email' , 'cpf', 'date_of_birth', 'cell']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'
        
        
class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Create
        fields = '__all__'