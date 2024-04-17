from django.db import models


# Create your models here.
class Visitor(models.Model):
    class Meta:
        verbose_name = "일일권 방문자"
        verbose_name_plural = "일일권 방문자"

    GENDER_CHOICE = (("M", "남자"), ("W", "여자"), ("X", "선택안함"))

    birth = models.CharField(verbose_name="생년월일", max_length=10)
    gender = models.CharField(
        verbose_name="성별", max_length=2, default="X", choices=GENDER_CHOICE
    )
    name = models.CharField(verbose_name="이름", max_length=30)
    address = models.CharField(
        max_length=150, verbose_name="주소", null=True, blank=True
    )
    phone = models.CharField(
        verbose_name="전화번호", max_length=15, null=True, blank=True
    )

    is_revisit = models.BooleanField(verbose_name="재방문 여부", default=False)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜")

    def __str__(self) -> str:
        return f"{self.created_at}에 방문한 {self.name}님"
