
from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import CustomUser
from users.serializers import UserSerializer


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
