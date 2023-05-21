from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.users.models import Token

User = get_user_model()


class RegisterUserSerializer(serializers.Serializer):
    """
    This serializer is used to register user
    """

    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)
    username = serializers.CharField(max_length=255, required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists() is True:
            raise serializers.ValidationError(
                _("A user is already registered with this e-mail address.")
            )
        return email

    def save(self):
        email = self.validated_data.get("email")
        password = self.validated_data.get("password")
        username = self.validated_data.get("username")

        user = User.objects.create(email=email, username=username, is_active=True)
        user.set_password(password)
        user.save()

        return user


class TokenSerializers(serializers.ModelSerializer):
    """
    This serializers is used to create token
    """

    class Meta:
        model = Token
        exclude = [
            "key",
        ]


class LoginUserSerializer(serializers.Serializer):
    """
    Login user serializers
    """

    email = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=128, required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists() is False:
            raise serializers.ValidationError(_("Email id doesnot exist in the system"))
        return email

    def validate(self, data):
        email = self.validate_email(data.get("email"))
        password = data.get("password")

        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(_({"error": "Invalid password"}))
        Token.objects.filter(user=user).delete()

        data["user"] = user
        return data
