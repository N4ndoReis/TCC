from django.contrib.auth.models import User
from tcc.models import Register,Login, Create, BringNote
from tcc.serializers import RegisterSerializer, CreateSerializer,BringNoteSerializer, RegisterSerializerV2
from rest_framework import viewsets, generics, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView 


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
    
    
class LoginView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        print(f"Email recebido: {email}")
        print(f"Senha recebida: {password}")

        if not email or not password:
            return Response({"error": "Email e senha são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            print(f"Usuário encontrado: {user}")
        except User.DoesNotExist:
            return Response({"error": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({"error": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)

        from rest_framework_simplejwt.tokens import RefreshToken
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class CreateViewSet(viewsets.ModelViewSet):
    queryset = Create.objects.all().order_by("id")
    serializer_class = CreateSerializer
    http_method_names = ["post"]

class BringNoteViewSet(viewsets.ModelViewSet):
    queryset = BringNote.objects.all().order_by("id")
    serializer_class = BringNoteSerializer
    http_method_names = ["get"]

