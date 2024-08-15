from django.urls import path

from apps.views import UserListCreateAPIView, ListingListCreateAPIView, CategoryListAPIView

urlpatterns = [
    path('user/', UserListCreateAPIView.as_view()),
    path('listing/', ListingListCreateAPIView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
]
