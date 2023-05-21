from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from apps.users.models import Token
from apps.users.serializers import (
    LoginUserSerializer,
    RegisterUserSerializer,
    TokenSerializers,
)

User = get_user_model()


class CreateUserAPI(CreateAPIView):
    """
    Register user and return token  with user details

    """

    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        return user

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        user_data = serializer.data
        token_data_dict = {
            "device_token": request.data.get("device_token"),
            "device_id": request.data.get("device_id"),
            "device_type": request.data.get("device_type"),
            "user": user.id,
        }

        token_serializer = TokenSerializers(data=token_data_dict)
        token_serializer.is_valid(raise_exception=True)
        token_data = token_serializer.save()
        user_data["key"] = token_data.key
        return Response({"status": HTTP_200_OK, "data": user_data}, status=HTTP_200_OK)


class LoginUserAPI(APIView):
    """
    Login user and return token with user details
    """

    permission_classes = (AllowAny,)

    def post(self, request):
        login_serializer = LoginUserSerializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        login_data = login_serializer.data
        user = login_serializer.validated_data["user"]
        token_data_dict = {
            "device_token": request.data.get("device_token"),
            "device_id": request.data.get("device_id"),
            "device_type": request.data.get("device_type"),
            "user": user.id,
        }
        token_serializer = TokenSerializers(data=token_data_dict)
        token_serializer.is_valid(raise_exception=True)
        token_data = token_serializer.save()
        login_data["key"] = token_data.key
        return Response({"status": HTTP_200_OK, "data": login_data}, status=HTTP_200_OK)


class LogoutUser(APIView):
    "Logout user by deleting it tokens"

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response(
            {"message": "token deleted successfully", "status": HTTP_200_OK},
            status=HTTP_200_OK,
        )
