from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.exceptions import ValidationError,PermissionDenied
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework import viewsets,generics,status
from .serializers import UserSerializer,CustomTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        username = self.request.data.get("username")
        email = self.request.data.get("email")
        
        if User.objects.filter(username=username).exists():
            raise ValidationError({'username': ['This username is already taken.']})
        if User.objects.filter(email=email).exists():
            raise ValidationError({'email': ['This email is already registered.']})
        
        serializer.save()
        
class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        if self.request.user == self.get_object() or self.request.user.is_superuser :
            serializer.save()
        else :
            raise PermissionDenied("You do not have permission to perform this action.")     
        
class AllProfile(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class LoginView(TokenObtainPairView):
    
    serializer_class = CustomTokenObtainPairSerializer
    
class LogoutView(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
                
            token = RefreshToken(refresh_token)
            token.blacklist()

            logout(request)
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
