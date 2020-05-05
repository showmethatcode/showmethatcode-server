from django.db import models


class Dog(models.Model):
    breed = models.CharField(max_length=20, verbose_name='견종')
    breed_kr = models.CharField(max_length=20, default='', verbose_name='견종')
    description = models.TextField(verbose_name='테스트 결과 설명')
    confidence = models.IntegerField(verbose_name='자신감')
    shyness = models.IntegerField(verbose_name='부끄러움')
    independence = models.IntegerField(verbose_name='자립심')
    positiveness = models.IntegerField(verbose_name='긍정 마인드')
    adaptability = models.IntegerField(verbose_name='적응력')
    image = models.URLField(max_length=200, verbose_name='이미지 경로', null=True)
    summary = models.CharField(max_length=20, verbose_name='요약')

class Question(models.Model):
    PERSONALITY_CHOICES = (
    (1, "Confidence"),
    (2, "Shyness"),
    (3, "Independence"),
    (4, "Positiveness"),
    (5, "Adaptability"),
)
    question = models.CharField(max_length=20, verbose_name='질문')
    personality = models.CharField(max_length=30, choices=PERSONALITY_CHOICES, verbose_name='성격')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='질문')
    text = models.CharField(max_length=200, verbose_name='텍스트')
    score = models.IntegerField(verbose_name='배점')
