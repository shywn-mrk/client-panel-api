from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from clients.models import Client
from .serializers import ClientSerializer

class ClientViewSet(viewsets.ViewSet):
    def list(self, request):
        # getting the user who is sending request
        user_token = request.auth
        user = Token.objects.get(key=user_token).user
        
        # filtering the clients base on the user
        queryset = Client.objects.all().filter(costumer=user)
        serializer = ClientSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk):
        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client)

        # IMPORTANT NOTE: users must see only their clients
        # they should not be able to see others
        # cheking to match for the right client

        # getting the user who is sending request
        user_token = request.auth
        user = Token.objects.get(key=user_token).user

        # checking if the right user is sending request
        if user == client.costumer:
            return Response(serializer.data)
        else:
            response = {
                'message': 'You are not allowed to see this client information',
                'success': False
            }

            return Response(response, status=HTTP_400_BAD_REQUEST)

