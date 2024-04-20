from rest_framework import serializers
from django.contrib.auth.models import User


class LoginUserRequestSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["id"]
