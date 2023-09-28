from django.contrib.auth import login, authenticate
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated
from .models import Doctor, Admin, CustomUser
from .serializers import AdminRegisterSerializer, AdminSerializer, CustomUserSerializer
from myapp.serializers import DoctorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class AdminRegisterView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'phone': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD),
                'workplace': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['username', 'phone', 'password', 'workplace'],
        ),
        operation_description="Admin register operation",
        responses={
            status.HTTP_201_CREATED: 'Registration successful',
            status.HTTP_400_BAD_REQUEST: 'Invalid data',
        }
    )
    def post(self, request):
        serializer = AdminRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Admin muvaffaqiyatli ro\'yxatdan o\'tdi'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminLoginView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD),
            },
            required=['username', 'password'],
        ),
        operation_description="Admin login operation",
        responses={
            status.HTTP_200_OK: 'Login successful',
            status.HTTP_401_UNAUTHORIZED: 'Invalid credentials',
        }
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'message': 'Tizimga muvaffaqiyatli kirdingiz'})
        else:
            return Response({'error': 'Noto\'g\'ri ma\'lumotlar'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # request.user.delete()
        request.session.flush()
        return Response({'message': 'Tizimdan muvaffaqiyatli chiqdingiz!'}, status=status.HTTP_200_OK)

class AdminUserView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AdminSerializer

    def get_queryset(self):
        return Admin.objects.filter(pk=self.request.user.pk)

class CustomUser(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer
