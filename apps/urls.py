from django.urls import path

from apps.views import UserListCreateView, ListingListCreateView

urlpatterns = [
    path('User/', UserListCreateView.as_view()),
    path('listing/', ListingListCreateView.as_view()),
]
