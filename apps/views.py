from rest_framework.generics import ListCreateAPIView

from apps.models import User
from apps.serializers import UserSerializer


# Create your views here.
class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
