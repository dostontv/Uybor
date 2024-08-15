from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView

from apps.filters import ListingFilter
from apps.models import User, Listing, Category
from apps.serializers import UserModelSerializer, CategorySerializer, \
    ListingListModelSerializer, ListingDetailModelSerializer


# Create your views here.
@extend_schema(tags=['auth'])
class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=['listing'])
class ListingListCreateView(ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingListModelSerializer
    filterset_class = ListingFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ListingDetailModelSerializer
        return super().get_serializer_class()


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
