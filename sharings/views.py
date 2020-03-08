from django.shortcuts import render

from django.http import HttpResponse
from sharings.models import Sharings

def sharings(request):
    return render(request, 'sharings.html')

def detail(request, sharing_id):
    return render(request, 'detail.html', {
        'id': sharing_id,
    })
