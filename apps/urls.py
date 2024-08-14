from django.urls import path

from apps.views import UserListCreateView, ListingListCreateView, CategoryListCreateView

urlpatterns = [
    path('User/', UserListCreateView.as_view()),
    path('listing/', ListingListCreateView.as_view()),
    path('category/', CategoryListCreateView.as_view()),
]
