# # from django.shortcuts import render
# # # Create your views here.
# from django.http import JsonResponse


# def index(request):
#     return JsonResponse({"ok": True, "data": "Hola mundo"})
from rest_framework.viewsets import ModelViewSet

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()  # select * from subscription
    serializer_class = SubscriptionSerializer
