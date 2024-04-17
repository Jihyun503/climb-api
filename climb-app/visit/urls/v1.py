from django.urls import path
from visit.views import v1

visit = v1.VisitViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = [
    path("", visit, name="visit"),
]
