from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from sharings.models import Sharing, SharingGroup
from django.urls import reverse
from django.contrib.auth import get_user_model, get_user
from users.models import User
import datetime


def detail(request, sharing_id):
    sharing_group = SharingGroup.objects.get(pk=sharing_id)
    sharings = sharing_group.sharing_set.all()
    if request.user.is_authenticated:
        is_team_member = request.user.is_team_member
    else:
        is_team_member = False
    # is_team_member = request.user.is_team_member if request.user.is_authenticated else False // 삼항연산자
    print(is_team_member)
    return render(request, 'detail.html', {
        'id': sharing_id,
        'date': sharing_group.date,
        'sharings': sharings,
        'is_team_member': is_team_member
    })

def home(request):
    if request.method =='GET':
        sharing_groups = SharingGroup.objects.all().order_by('-date')[:7]
        can_check_in = False
        is_team_member = False
        if request.user.is_authenticated:
            sharing_today = Sharing.objects.filter(user=request.user,   created_at__date=datetime.date.today())
            is_team_member = request.user.is_team_member
            if is_team_member and len(sharing_today) == 0:
                can_check_in = True
        return render(request, 'sharings.html', {
            'groups': sharing_groups,
            'can_check_in': can_check_in,
        })


def write(request):
    if request.method == 'POST':
        created_at = request.POST.get('created_at', '')
        til = request.POST.get('til', '')
        action_plan = request.POST.get('action_plan', '')
        is_secret = request.POST.get('is_secret', '')  == 'on'
        print(is_secret)
        error_message = ''

        if til == '':
            error_message = 'TIL을 작성하시오'

        if action_plan == '':
            error_message = 'Action Plan을 작성하시오'

        user = get_user(request)
        date = datetime.datetime.now().date() # ex) 2020-03-20

        sharing_group, flag = SharingGroup.objects.get_or_create(date=date)
        group_id = sharing_group.id

        if not error_message and user.is_authenticated:
            sharings = Sharing.objects.create(created_at=created_at, til=til, action_plan=action_plan, user=user, sharing_id=group_id, is_secret=is_secret)
            sharings.save()
            return redirect('/sharings')
        else:
            return render(request, 'sharings.html', {
                'error_message': error_message
            })

def edit_form(request, sharing_id):
    is_authenticated = request.user.is_authenticated
    is_team_member = False
    sharing_group = SharingGroup.objects.filter(id=sharing_id).get()
    if is_authenticated:
        is_team_member = request.user.is_team_member
        try:
            sharing = sharing_group.sharing_set.all().filter(user=user).get()
        except NameError as e:
            error_message = e
            return error_message
    return render(request, 'edit.html', {
        'id': sharing_id,
        'date': sharing_group.date,
        'sharing': sharing,
        'is_team_member': is_team_member
    })

def edit(request, sharing_id):
    til = request.POST.get('til', '')
    action_plan = request.POST.get('action_plan', '')
    user = get_user(request)
    sharing_group = SharingGroup.objects.get(pk=sharing_id)
    sharing = sharing_group.sharing_set.get(user_id=user)
    sharing.til = til
    sharing.action_plan = action_plan
    sharing.save()

    return redirect('/sharings/{}'.format(sharing_id))
