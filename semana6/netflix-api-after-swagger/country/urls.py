from django.urls import path

from .views import create_countries, delete_countries

urlpatterns = [
    path("country/create", create_countries),
    path("country/delete", delete_countries),
]
