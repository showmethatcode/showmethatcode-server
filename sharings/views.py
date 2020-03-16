from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from sharings.models import Sharings
from django.urls import reverse
from django.contrib.auth import get_user_model, get_user

# views = 비지니스 로직
def detail(request, sharing_id):
    return render(request, 'detail.html', {
        'id': sharing_id,
    })


def detail_temp(request):
    return HttpResponseRedirect('/detail/1')


def home(request):
    if request.method =='GET':
        return render(request, 'sharings.html')


def write(request):
    if request.method == 'POST':
        created_at = request.POST.get('created_at', '')
        til = request.POST.get('til', '')
        action_plan = request.POST.get('action_plan', '')

        error_message = ''

        if til == '':
            error_message = 'TIL을 작성하시오'
            
        if action_plan == '':
            error_message = '내일 무엇을 할거죠?'

        user = get_user(request)
    
        if not error_message and user.is_authenticated:
            sharings = Sharings.objects.create(created_at=created_at, til=til, action_plan=action_plan, user=user)
            sharings.save()
            return redirect('/')
        else:
            return render(request, 'sharings.html', {
                'error_message': error_message
            })

