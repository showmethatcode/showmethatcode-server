from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.templatetags.static import static


class UserManager(UserManager):
    def create_user(self, *args, **kwargs):
        team_members = [
            'softkey95@gmail.com',
            'incleaf@gmail.com',
            'koreanhoseon@gmail.com',
            'qpwpep5429@gmail.com'
        ]
        kwargs['is_team_member'] = True if kwargs['email'] in team_members else False
        return super(UserManager, self).create(*args, **kwargs)


class User(AbstractBaseUser):
    email = models.CharField(unique=True, max_length=200, verbose_name='유저아이디')
    is_team_member = models.BooleanField(verbose_name='팀 멤버 유무', default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def user_profile_images(self):
        get_user_profile_images = {
            'softkey95@gmail.com': static('images/woosik.png'),
            'incleaf@gmail.com': static('images/hyeonsu.png'),
            'koreanhoseon@gmail.com': static('images/hoseon.png'),
            'qpwpep5429@gmail.com': static('images/sangmin.png'),
        }
        return get_user_profile_images[self.email]
