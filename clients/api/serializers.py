from rest_framework import serializers
from clients.models import Client
from accounts.api.serializers import UserSerializer

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'customer',
            'first_name',
            'last_name',
            'email',
            'phone',
            'balance'
        )
        depth = 1
