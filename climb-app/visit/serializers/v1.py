from visit.models import Visitor
from rest_framework import serializers


### Request
class VisitorRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=150)
    gender = serializers.ChoiceField(choices=(("M", "남자"), ("W", "여자")))
    phone = serializers.CharField(max_length=15)
    birth = serializers.CharField(max_length=10)
    is_revisit = serializers.BooleanField()


### Response
class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        exclude = ["id"]
