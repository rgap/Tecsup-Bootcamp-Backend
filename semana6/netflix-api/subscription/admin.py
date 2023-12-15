from django.contrib import admin

from .models import Subscription

# Esto lo agrega al admin
admin.site.register(Subscription)
