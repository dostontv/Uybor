from django.urls import path

from apps.views import UserListCreateView

urlpatterns = [
    path('User/', UserListCreateView.as_view()),
]
