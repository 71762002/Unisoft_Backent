from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import permissions, status, generics
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import logout
from user.serializer import *
from .models import User


from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


class SupportUserWritePermission(BasePermission):
    message = 'Xabarlarni tahrirlash faqat muallifga tegishli!'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user
    

@swagger_auto_schema(method="POST", tags=['user'], request_body=UserRegisterSerializer)
@api_view(['POST'])
def registratsiya(request, *args, **kwargs):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)   
    serializer.save()
    return Response({
        'status' : True,
        "data" : serializer.data,
        
    })  


@swagger_auto_schema(method="POST", tags=['user'], request_body=UserLoginSerializer)
@api_view(["POST"])
def user_login(request, *args, **kwargs):
    email = request.data['email']
    password = request.data['password']
    user = User.objects.filter(email=email).first()
    if not user or not user.check_password(password):
        return Response({
            "status" : False,
            'error' : "User not found"
        }, status=HTTP_400_BAD_REQUEST)
    user_tokens = user.tokens()


    return Response({
        "status" : True,
        "email": email,
        "password" : password,
        "access_token" : user_tokens.get('access'),
        "refresh_token" : user_tokens.get('refresh') 
    })
  

@swagger_auto_schema(method="GET", tags=['user'], query_serializer=UserSerializer)
@api_view(["GET"])
def get_user(request, *args, **kwargs):
    if not request.user.is_authenticated:                                     # Foydalanuvchi tizimga kirganligini tekshirish
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    
    role = request.user.role               # Foydalanuvchi rolini olish
    queryset = User.objects.all()
    if role == 'manager':
        queryset = queryset.filter(role='manager')
    elif role == 'operator':
        queryset = queryset.filter(id=request.user.id)
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)



# def get_queryset(self):
#         if self.request.user.is_superuser:
#             return User.objects.all()
#         else:
#             return User.objects.filter(id=self.request.user.id)

    

class UserLagout(APIView):
    def post(self, request):
        logout(request)
        return Response(status=HTTP_200_OK)
    



