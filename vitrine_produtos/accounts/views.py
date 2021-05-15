from django.shortcuts import redirect
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from vitrine_produtos.validation_messages import invalid_email, \
    email_already_used, user_successfully_created, \
    field_is_missing

from .models import User, Profile
from .serializers import UserSerializer, TokenSerializer, \
    UserLoginSerializer, Token


class AuthenticationAPIView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        empty_field = None

        if request.data.get('email') is None:
            empty_field = 'email'
        elif request.data.get('password') is None:
            empty_field = 'password'

        if empty_field is not None:
            return Response(
                field_is_missing(empty_field),
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'username': request.data.get('email'),
            'email': request.data.get('email'),
            'password': request.data.get('password')
        }

        serializer = self.get_serializer_class()(data=data)

        if serializer.is_valid():
            user = serializer.user
            token, _ = Token.objects.get_or_create(user=user)

            data = TokenSerializer(token).data

            data['user'] = self.prepare_user_data(user)

            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def prepare_user_data(self, user):
        data = dict()

        data['id'] = user.id

        profile = Profile.objects.get(user_id=user.id)

        data['name'] = profile.name
        data['email'] = user.email
        data['role'] = profile.role

        return data


class UserApiView(GenericAPIView):
    def post(self, request):
        try:
            request.data['name']
            request.data['email']
            request.data['password']
            request.data['role']
        except Exception as e:
            return Response(
                field_is_missing(e.__str__()),
                status=status.HTTP_400_BAD_REQUEST
            )

        data = request.data

        if not data['email'].find('@'):
            return Response(
                invalid_email(),
                status=status.HTTP_400_BAD_REQUEST
            )

        test_user = User.objects.filter(
            email=data['email']
        ).first()

        if test_user is not None:
            return Response(
                email_already_used(),
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            new_user = User.objects.create_user(
                email=data['email'],
                password=data['password'],
                username=data['email'],
            )

            Profile.objects.create(
                user=new_user,
                role=data['role'],
                name=data['name']
            )

            return Response(
                user_successfully_created(),
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
