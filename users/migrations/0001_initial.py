# Generated by Django 3.0.4 on 2020-03-22 12:39

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(unique=True, max_length=200, verbose_name='유저아이디')),
                ('is_team_member', models.BooleanField(default=False, verbose_name='팀 멤버 유무')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
