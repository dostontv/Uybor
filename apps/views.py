import random

from django.core.cache import cache
from django.http import HttpResponse
from django.views import View
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, ListAPIView

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
class ListingListCreateAPIView(ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingListModelSerializer
    filterset_class = ListingFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ListingDetailModelSerializer
        return super().get_serializer_class()


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SendCodeView(View):
    def get(self, request, *args, **kwargs):
        phone_number = request.GET.get('phone_number')

        code = cache.get(phone_number)
        if not code:
            code = str(random.randint(100000, 999999))

            cache.set(phone_number, code, timeout=120)
        else:
            return HttpResponse(f"Oldingi kod hali ham yaroqli: {code}")

        return HttpResponse(f"Yangi kod: {code}")
