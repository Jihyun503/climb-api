from visit.models import Visitor
from datetime import datetime


class VisitManager:
    def get_visitor(self, queryset, request_data):
        keyword = request_data.query_params.get("keyword", None)
        date = request_data.query_params.get("date", None)

        if queryset.exists():
            if keyword:
                queryset = queryset.filter(name=keyword)
            if date:
                date = datetime.strptime(date, "%Y%m%d").date()
                queryset = queryset.filter(created_at__date=date)

        return queryset

    def create_visit_data(self, validated_data):
        name = validated_data["name"]
        address = validated_data["address"]
        gender = validated_data["gender"]
        phone = validated_data["phone"]
        birth = validated_data["birth"]
        is_revisit = validated_data["is_revisit"]

        try:
            instance = Visitor.objects.create(
                name=name,
                address=address,
                gender=gender,
                phone=phone,
                birth=birth,
                is_revisit=is_revisit,
            )
        except Exception:
            return False, "일일권 등록에 실패하였습니다.", None

        return True, "", instance.name
