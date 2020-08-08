from rest_framework import serializers
from user_settings.models import Settings
from accounts.api.serializers import UserSerializer

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = (
            'id',
            'user',
            'allow_registeration',
            'disable_balance_on_add',
            'disable_balance_on_edit'
        )
        depth = 1
