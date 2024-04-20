from django.urls import include, path

urlpatterns = [
    path("visit/", include("visit.urls.v1")),
    path("auth/", include("user.urls.v1")),
]
