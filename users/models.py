from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class UserManager(UserManager):
    def create_user(self, *args, **kwargs):
        team_members = [
            'softkey95@gmail.com',
            'incleaf@gmail.com',
            'koreanhoseon@gmail.com',
        ]
        kwargs['is_team_member'] = True if kwargs['email'] in team_members else False
        print(kwargs['is_team_member'])
        return super(UserManager, self).create(*args, **kwargs)

class User(AbstractBaseUser):
    email = models.CharField(unique=True, verbose_name='유저아이디')
    is_team_member = models.BooleanField(verbose_name='팀 멤버 유무', default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
