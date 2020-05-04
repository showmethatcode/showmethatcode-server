from django.db import models


class Dogs(models.Model):
    breed = models.CharField(max_length=20, verbose_name='강아지 타입')
    description = models.TextField(null=True, verbose_name='테스트 결과 설명')
    confidence = models.IntegerField(null=True, verbose_name='자신감')
    shyness = models.IntegerField(null=True, verbose_name='부끄러움')
    independence = models.IntegerField(null=True, verbose_name='자립심')
    positiveness = models.IntegerField(null=True, verbose_name='긍정 마인드')
    adaptability = models.IntegerField(null=True, verbose_name='적응력')

class UserStats(models.Model):
    confidence = models.IntegerField(null=True, verbose_name='자신감')
    shyness = models.IntegerField(null=True, verbose_name='부끄러움')
    independence = models.IntegerField(null=True, verbose_name='자립심')
    positiveness = models.IntegerField(null=True, verbose_name='긍정 마인드')
    adaptability = models.IntegerField(null=True, verbose_name='적응력')
    doggy = models.CharField(max_length=20, verbose_name='강아지')

class Question(models.Model):
    question = models.CharField(max_length=20, verbose_name='질문')


