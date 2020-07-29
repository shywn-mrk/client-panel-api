from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from clients.models import Client
from .serializers import ClientSerializer
from accounts.api.serializers import UserSerializer

class ClientViewSet(viewsets.ViewSet):
    def list(self, request):
        # getting the user who is sending request
        user_token = request.auth
        user = Token.objects.get(key=user_token).user
        
        # filtering the clients base on the user
        queryset = Client.objects.all().filter(customer=user)
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
        if user == client.customer:
            return Response(serializer.data)
        else:
            response = {
                'message': 'You are not allowed to see this client information',
                'success': False
            }

            return Response(response, status=HTTP_400_BAD_REQUEST)

    
    def create(self, request):
        # getting the user who is sending request
        user_token = request.auth
        user = Token.objects.get(key=user_token).user

        # create new client
        data = {
            'customer': user,
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'phone': request.data.get('phone'),
            'balance': float(request.data.get('balance'))
        }

        serializer = ClientSerializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            Client.objects.create(**data)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        # getting the user who is sending request
        user_token = request.auth
        user = Token.objects.get(key=user_token).user

        data = {
            'customer': user,
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'phone': request.data.get('phone'),
            'balance': float(request.data.get('balance'))
        }

        serializer = ClientSerializer(data=data)
    
        if serializer.is_valid(raise_exception=True):
            client = Client.objects.get(pk=pk)
            client.__dict__.update(**data)
            client.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


        def destroy(self, request, pk=None):
            pass
