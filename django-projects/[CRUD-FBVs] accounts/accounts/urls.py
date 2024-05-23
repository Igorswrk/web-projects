from django.urls import path

from .views import (
    home_view,
    user_signup_view,
    login_view,
    logout_view,
    user_list_view,
    user_profile_view,
    user_delete_view,
    user_update_view
)

urlpatterns = [
    path("", home_view, name="home"),
    path("signup/", user_signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("users/", user_list_view, name="users"),
    path("update/<int:id>", user_update_view, name="update"),
    path("delete/<int:id>", user_delete_view, name="delete"),
    path("users/<int:id>", user_profile_view, name="profile"),
]
