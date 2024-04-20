from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    # 회원가입
    def register(self, request):
        return Response()

    def login(self, request):
        return Response()
