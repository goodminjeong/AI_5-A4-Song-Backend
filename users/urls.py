from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", views.UserView.as_view(), name="user_all_view"),
    path("signup/", views.UserView.as_view(), name="user_view"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/<int:user_id>/", views.ProfileView.as_view(), name="profile_view"),
    path("<int:user_id>/photos/", views.UserPhotoView.as_view()),
    path("kakao/", views.KakaoLogin.as_view(), name="kakao_login"),
    path("google/", views.GoogleLogin.as_view(), name="google_login"),
    path("naver/", views.NaverLogin.as_view(), name="naver_login"),
]
