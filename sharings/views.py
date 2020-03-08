from django.shortcuts import render, HttpResponseRedirect

from django.http import HttpResponse
from sharings.models import Sharings
from django.urls import reverse


# views = 비지니스 로직

def sharings(request):
    return render(request, 'sharings.html')

def detail(request, sharing_id):
    return render(request, 'detail.html', {
        'id': sharing_id,
    })


def detail_temp(request):
    return HttpResponseRedirect('/detail/1')
