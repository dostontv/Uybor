from django.urls import path

from apps.views import UserCreateAPIView, ListingListCreateAPIView, CategoryListAPIView

urlpatterns = [
    path('user/', UserCreateAPIView.as_view()),
    path('listing/', ListingListCreateAPIView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
]
