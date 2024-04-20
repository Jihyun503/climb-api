from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from user.serializers.v1 import LoginUserRequestSerializer, UserResponseSerializer
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    """
        POST v1/user/register/
        회원가입
    """

    def register(self, request):

        return Response()

    """
        POST v1/user/login/
        로그인
    """

    def login(self, request):
        req_serializer = LoginUserRequestSerializer(data=request.data)

        if req_serializer.is_valid() is False:
            return Response(
                {
                    "message": "필수 파라미터 오류",
                    "error": req_serializer.errors,
                    "code": 100,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        username = req_serializer.validated_data["id"]
        password = req_serializer.validated_data["password"]

        try:
            user = User.objects.get(username=username, is_active=True)
        except User.DoesNotExist:
            return Response(
                {
                    "message": "유효하지 않은 회원입니다.",
                    "code": 100,
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except User.MultipleObjectsReturned:
            return Response(
                {
                    "message": "유효하지 않은 계정입니다.",
                    "code": 100,
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        is_valid = user.check_password(password)

        if not is_valid:
            return Response(
                {
                    "message": "유효하지 않은 비밀번호입니다.",
                    "code": 100,
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token, _ = Token.objects.get_or_create(user=user)

        user_serializer = UserResponseSerializer(user)

        return Response(data={"user": user_serializer.data, "token": token.key})

    """
        DELETE v1/user/logout/
        로그아웃
    """

    def logout(self, request):
        return Response()
