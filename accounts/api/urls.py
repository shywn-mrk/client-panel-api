from django.urls import path
from accounts.api.views import UserCreateAPIView, UserLoginAPIView

urlpatterns = [
    path('signup/', UserCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login')
]