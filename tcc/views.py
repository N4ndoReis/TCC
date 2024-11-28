from tcc.models import Register,Login, Create, BringNote
from tcc.serializers import RegisterSerializer, LoginSerializer, CreateSerializer,BringNoteSerializer, RegisterSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all().order_by("id")
    # serializer_class = RegisterSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'email']
    http_method_names = ["post"]
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return RegisterSerializerV2
        return RegisterSerializer
    
    
class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all().order_by("id")
    serializer_class = LoginSerializer
    http_method_names = ["post"]

class CreateViewSet(viewsets.ModelViewSet):
    queryset = Create.objects.all().order_by("id")
    serializer_class = CreateSerializer
    http_method_names = ["post"]

class BringNoteViewSet(viewsets.ModelViewSet):
    queryset = BringNote.objects.all().order_by("id")
    serializer_class = BringNoteSerializer
    http_method_names = ["get"]

