from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

from .views import UserRegisterView, ProfileView

urlpatterns = [
    path("api/auth/login/", TokenObtainPairView.as_view()),
    path("api/auth/refresh/", TokenRefreshView.as_view()),
    path("register/", UserRegisterView.as_view()),
    path("register/profile/", ProfileView.as_view()),
]
