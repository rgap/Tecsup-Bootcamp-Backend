from rest_framework.serializers import ModelSerializer

from .models import Actor


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        # fields = ("id", "title")
        fields = "__all__"
