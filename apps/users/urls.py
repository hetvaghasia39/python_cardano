from django.urls import path

from apps.users.views import CreateUserAPI, LoginUserAPI

urlpatterns = [
    path("create_user/", CreateUserAPI.as_view(), name="create_user_api"),
    path("login_user/", LoginUserAPI.as_view(), name="login_user_api"),
]
