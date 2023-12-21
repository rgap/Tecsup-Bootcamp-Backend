from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Actor
from .serializers import ActorSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()  # select * from Actor
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated]
