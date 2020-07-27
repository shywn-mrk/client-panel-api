from rest_framework import serializers
from user_settings.models import Settings
from accounts.api.serializers import UserSerializer

class SettingsSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Settings
        fields = (
            'user',
            'allow_registeration',
            'disable_balance_on_add',
            'disable_balance_on_edit'
        )

    def get_user(self, setting):
        serializer = UserSerializer(setting.user)
        return serializer.data
