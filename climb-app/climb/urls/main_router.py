from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include("climb.urls.v1")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r"^__debug__/", include(debug_toolbar.urls)),
    ]
