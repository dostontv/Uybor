from django.contrib.auth.mixins import LoginRequiredMixin
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.filters import ListingFilter
from apps.models import User, Listing, Category
from apps.serializers import UserModelSerializer, CategorySerializer, \
    ListingListModelSerializer, ListingDetailModelSerializer


# Create your views here.
@extend_schema(tags=['auth'])
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    # permission_classes = [IsAuthenticated]


@extend_schema(tags=['listing'])
class ListingListCreateAPIView(ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingListModelSerializer
    filterset_class = ListingFilter

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, moderation_status=Listing.MSType.A)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ListingDetailModelSerializer
        return super().get_serializer_class()


@extend_schema(tags=['category'])
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
