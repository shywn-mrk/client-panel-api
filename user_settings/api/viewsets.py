from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
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


    def update(self, request, pk=None):
        # getting the user who is sending request
        user_token = request.auth
        user = Token.objects.get(key=user_token).user

        # getting the sent data
        data = {
            "user": user,
            "allow_registeration": request.data.get('allow_registeration'),
            "disable_balance_on_add": request.data.get('disable_balance_on_add'),
            "disable_balance_on_edit": request.data.get('disable_balance_on_edit')
        }

        serializer = SettingsSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            settings = Settings.objects.get(pk=pk)
            settings.__dict__.update(**data)
            settings.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
