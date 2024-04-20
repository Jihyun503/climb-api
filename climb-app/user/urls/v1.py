from django.urls import path
from user.views.v1 import AuthViewSet

register = AuthViewSet.as_view({"post": "register"})
login = AuthViewSet.as_view({"post": "login"})


urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
]
