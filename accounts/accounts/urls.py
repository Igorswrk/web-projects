from django.urls import path

from .views import (
    home_view,
    user_signup_view,
    login_view,
    logout_view,
    user_list_view,
    user_profile_view
)

urlpatterns = [
    path("", home_view, name="home"),
    path("signup/", user_signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("users/", user_list_view, name="users"),
    path("users/<int:pk>", user_profile_view, name="user"),
]
