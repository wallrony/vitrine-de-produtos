from django.contrib.auth import authenticate, password_validation
from vitrine_produtos.accounts.models import User, Profile
from rest_framework.authtoken.models import Token
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(source='get_full_name', required=True)
    email = serializers.CharField(required=True,)

    class Meta:
        model = User
        fields = ('id', 'name', 'email')


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    default_error_messages = {
        'inactive_account': 'this accounts is inactive',
        'invalid_credentials': 'the provided credentials are invalid'
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)

    def validate(self, data):
        self.user = authenticate(
            username=data.get('username'),
            password=data.get('password')
        )

        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(
                    self.error_messages['inactive_account']
                )

            return self.user
        raise serializers.ValidationError(
            self.error_messages['invalid_credentials']
        )


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')
    user = UserSerializer(read_only=True)

    class Meta:
        model = Token
        fields = ('auth_token', 'user', 'created')
