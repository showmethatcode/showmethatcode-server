from django.db import models
from users.models import User

class Sharings(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성 시 현재 시간 자동저장
    til = models.TextField() # 길이 제한 없이 생성
    action_plan = models.TextField() # 길이 제한 없이 생성
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    