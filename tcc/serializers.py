from rest_framework import serializers
from tcc.models import Register,Login,Create

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['name', 'email' , 'cpf', 'date_of_birth', 'cell']
    
    def validate_cpf(self,cpf):
            if len(cpf) != 11:
                    raise serializers.ValidationError('O CPF deve ter 11 dígitos!')
            return cpf 

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'
        
        
class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Create
        fields = '__all__'