from visit.models import Visitor


class VisitManager:
    def get_visitor(self):
        return None

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
