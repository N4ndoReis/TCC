from tcc.models import Register,Login, Create
from tcc.serializers import RegisterSerializer, LoginSerializer, CreateSerializer
from rest_framework import viewsets

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class CreateViewSet(viewsets.ModelViewSet):
    queryset = Create.objects.all()
    serializer_class = CreateSerializer

