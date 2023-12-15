from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("actor.urls")),
    path("api/v1/", include("subscription.urls")),
    path("api/v1/", include("content.urls")),
]
