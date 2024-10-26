from tcc.models import Register,Create
from tcc.serializers import RegisterSerializer, CreateSerializer
from rest_framework import viewsets

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class CreateViewSet(viewsets.ModelViewSet):
    queryset = Create.objects.all()
    serializer_class = CreateSerializer

