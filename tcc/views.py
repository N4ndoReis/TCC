from tcc.models import Register,Login, Create, BringNote
from tcc.serializers import RegisterSerializer, LoginSerializer, CreateSerializer,BringNoteSerializer, RegisterSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    # serializer_class = RegisterSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'email']
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return RegisterSerializerV2
        return RegisterSerializer
    
class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class CreateViewSet(viewsets.ModelViewSet):
    queryset = Create.objects.all()
    serializer_class = CreateSerializer

class BringNoteViewSet(viewsets.ModelViewSet):
    queryset = BringNote.objects.all()
    serializer_class = BringNoteSerializer

