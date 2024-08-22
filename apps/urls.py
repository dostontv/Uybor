from django.urls import path

from apps.views import UserListCreateAPIView, ListingListCreateAPIView, CategoryListAPIView, SendCodeView

urlpatterns = [
    path('user/', UserListCreateAPIView.as_view()),
    path('listing/', ListingListCreateAPIView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
    path('send-code/', SendCodeView.as_view(), name='send_code'),
]
