from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from user_settings.models import Settings

class UserCreateSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'token']
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }


    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']

        user = User(username=username)
        user.set_password(password)
        user.save()

        settings = Settings(user=user)
        settings.save()

        token = Token.objects.create(user=user)
        validated_data['token'] = token.key

        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password', 'token']
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }


    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            data['token'] = 'some random token'
        else:
            raise ValidationError('wrong username or password')

        token = Token.objects.filter(user=user)

        data['token'] = token.first().key

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
        )
