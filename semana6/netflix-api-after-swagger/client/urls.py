from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r"client", ClientViewSet)
router.register(r"profile", ProfileViewSet)

urlpatterns = [path("", include(router.urls))]
