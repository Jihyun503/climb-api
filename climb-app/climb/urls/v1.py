from django.urls import include, path

urlpatterns = [
    path("visit/", include("visit.urls.v1")),
]
