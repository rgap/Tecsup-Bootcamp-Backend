from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ContentViewSet

router = DefaultRouter()

router.register(r"content", ContentViewSet)

urlpatterns = [path("", include(router.urls))]
