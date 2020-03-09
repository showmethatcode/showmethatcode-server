from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class UserManager(UserManager):
    def create_user(self, *args, **kwargs):
        team_members = [
            'softkey95@gmail.com',
        ]
        kwargs['is_team_member'] = True if kwargs['email'] in team_members else False
        print(kwargs['is_team_member'])
        return super(UserManager, self).create(*args, **kwargs)

class User(AbstractBaseUser):
    email = models.TextField(unique=True, verbose_name='유저아이디')
    is_team_member = models.BooleanField(verbose_name='팀 멤버 유무', default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
# "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "last_name" varchar(150) NOT NULL)
