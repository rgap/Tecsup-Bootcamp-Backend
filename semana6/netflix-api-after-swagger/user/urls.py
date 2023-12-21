from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserViewSet

router = DefaultRouter()
router.register(r"user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("token", TokenObtainPairView.as_view(), name="Get JWT"),
    path("token/refresh", TokenRefreshView.as_view(), name="Refresh JWT"),
]
