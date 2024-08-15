from django.urls import path

from apps.views import UserListCreateAPIView, ListingListCreateView, CategoryListCreateView

urlpatterns = [
    path('user/', UserListCreateAPIView.as_view()),
    path('listing/', ListingListCreateView.as_view()),
    path('category/', CategoryListCreateView.as_view()),
]
