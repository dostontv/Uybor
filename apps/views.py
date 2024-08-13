from rest_framework.generics import ListCreateAPIView

from apps.models import User, Listing
from apps.serializers import UserSerializer, ListingSerializer


# Create your views here.
class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListingListCreateView(ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer