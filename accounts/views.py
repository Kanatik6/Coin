from rest_framework.viewsets import generics, ModelViewSet

from accounts.serializers import UserSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
