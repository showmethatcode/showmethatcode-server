from django.db import models
from django.contrib.auth.models import User

class User(models.AbstractBaseUser):
    is_team_member = models.BooleanField(verbose_name='팀 멤버 유무', default=False)

class UserManager(BaseUserManager):
    def create(self, *args, **kwargs):
        team_members = [
            'softkey95@gmail.com',
        ]
        kwargs['is_team_member'] = True if kwargs['email'] in team_members else False
    return super(UserManager, self).create(*args, **kwargs)



# Create your models here.
