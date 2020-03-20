from django.db import models
from users.models import User


class SharingGroup(models.Model):
    date = models.DateField(auto_now_add=True)
#sharebyuser_set.create

class Sharing(models.Model):
    sharing = models.ForeignKey(SharingGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    til = models.TextField() # 길이 제한 없이 생성
    action_plan = models.TextField() # 길이 제한 없이 생성
    created_at = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성 시 현재 시간 자동저장
