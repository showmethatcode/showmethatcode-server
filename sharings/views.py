from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from sharings.models import Sharing, SharingGroup
from django.urls import reverse
from django.contrib.auth import get_user_model, get_user
import datetime

#s views = 비지니스 로직
def detail(request, sharing_id):
    sharing_group = SharingGroup.objects.get(pk=sharing_id)
    sharings = sharing_group.sharing_set.all()
    return render(request, 'detail.html', {
        'id': sharing_id,
        'date': sharing_group.date,
        'sharings': sharings
    })


def detail_temp(request):
    return HttpResponseRedirect('/detail/1')


def home(request):
    if request.method =='GET':
        sharing_groups = SharingGroup.objects.all().order_by('-date')[:7]
        sharing_today = Sharing.objects.filter(user=request.user, created_at__date=datetime.date.today())
        can_check_in = len(sharing_today) == 0

        return render(request, 'sharings.html', {
            'groups': sharing_groups,
            'can_check_in': can_check_in,
        })


def write(request):
    if request.method == 'POST':
        created_at = request.POST.get('created_at', '')
        til = request.POST.get('til', '')
        action_plan = request.POST.get('action_plan', '')
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
            sharings = Sharing.objects.create(created_at=created_at, til=til, action_plan=action_plan, user=user, sharing_id=group_id)
            sharings.save()
            return redirect('/')
        else:
            return render(request, 'sharings.html', {
                'error_message': error_message
            })