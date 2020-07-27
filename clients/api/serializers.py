from rest_framework import serializers
from clients.models import Client
from accounts.api.serializers import UserSerializer

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    costumer = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Client
        fields = (
            'id',
            'costumer',
            'first_name',
            'last_name',
            'email',
            'phone',
            'balance'
        )

    def get_costumer(self, client):
        serializer = UserSerializer(client.costumer)
        return serializer.data

    
