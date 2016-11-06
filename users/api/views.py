from rest_framework import viewsets

from users.models import UserInfo
from .serializers import UserInfoSerializer


# For rest frame work api calls
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
