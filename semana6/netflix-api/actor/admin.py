from django.contrib import admin

from .models import Actor

# Esto lo agrega al admin
admin.site.register(Actor)
