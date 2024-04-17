from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from visit.models import Visitor
from visit.serializers.v1 import VisitorSerializer, VisitorRequestSerializer
from visit.helper.visit import VisitManager
from django.db import transaction


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    permission_classes = [AllowAny]
    serializer_class = VisitorSerializer
    visit_manager = VisitManager()

    def list(self, request):
        serializer = self.get_serializer(self.queryset, many=True)

        return Response(serializer.data)

    @transaction.atomic
    def create(self, request):
        req_serializer = VisitorRequestSerializer(data=request.data)

        if req_serializer.is_valid() is False:
            return Response(
                {
                    "message": "필수 파라미터 오류",
                    "error": req_serializer.errors,
                    "code": 100,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        result, error, name = self.visit_manager.create_visit_data(
            req_serializer.validated_data
        )

        if result is False:
            return Response(
                {"message": error, "code": 101}, status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                "code": 200,
                "message": "일일권 등록이 완료되었습니다.",
                "data": {"name": name},
            }
        )
