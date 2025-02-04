from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register', CreateUserView.as_view(), name="register"),
    path('login', TokenObtainPairView.as_view(), name="login"),
    path('refresh', TokenRefreshView.as_view(), name="refresh_token"),
    path('logout', LogoutView.as_view(), name="logout")
]