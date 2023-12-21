from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Content
from .serializers import ContentSerializer


class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()  # select * from Actor
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]
