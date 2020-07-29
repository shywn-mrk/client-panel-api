from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_settings.models import Settings
from .serializers import SettingsSerializer

class SettingsViewSet(viewsets.ViewSet):
    def list(self, request):
        # getting the user who is sending request
        user_token = request.auth
        user = Token.objects.get(key=user_token).user

        # getting the settings for that user
        settings = Settings.objects.get(user=user)
        serializer = SettingsSerializer(settings)

        return Response(serializer.data)
