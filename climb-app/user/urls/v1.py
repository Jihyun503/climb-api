from django.urls import path
from user.views.v1 import UserViewSet

register = UserViewSet.as_view({"post": "register"})
login = UserViewSet.as_view({"post": "login"})


urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
]
