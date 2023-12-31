from rest_framework.serializers import ModelSerializer
from subscription.serializers import SubscriptionSerializer
from user.serializers import UserSerializer

from .models import Client, Profile


class ClientSerializer(ModelSerializer):
    # user = UserSerializer(read_only=True)
    # subscription = SubscriptionSerializer(read_only=True)

    class Meta:
        model = Client
        # fields = ["created_at", "updated_at", "user", "payment_date", "subscription"]
        fields = "__all__"


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
