from django.contrib.auth.hashers import make_password  # hashes the password
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    # Para mostrar jsons autogenerados
    class Meta:
        model = User
        fields = "__all__"
