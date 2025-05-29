from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
