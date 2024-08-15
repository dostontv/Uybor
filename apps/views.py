from rest_framework.generics import ListCreateAPIView

from apps.filters import ListingFilter
from apps.models import User, Listing, Category
from apps.serializers import UserSerializer, ListingSerializer, CategorySerializer


# Create your views here.
class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListingListCreateView(ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filterset_class = ListingFilter


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
