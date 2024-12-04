from rest_framework import serializers
from tcc.models import Register,Login,Create, BringNote
from tcc.validators import invalid_name, invalid_cell
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
    
    def validate(self,data):
        if invalid_name(data['name']):
            raise serializers.ValidationError({'name':'O nome deve conter apenas letras e espaços.'})
        if invalid_cell(data['cell']):
            raise serializers.ValidationError({'cell':'O celular precisa seguir o modelo: 86 99999-9999 (respeitando traços e espaços).'})
        
        password = data.get('password', '')
        if len(password) < 8:
            raise serializers.ValidationError({
                'password': 'A senha deve ter no mínimo 8 caracteres!'
            })

        data['password'] = make_password(password)

        return data
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'       
        
class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Create
        fields = '__all__'

class BringNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BringNote
        fields = '__all__'
        
        
# versioning        
class RegisterSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id','name','email','cell']