from django.shortcuts import render

from django.http import HttpResponse
from sharings.models import Sharings

# views = 비지니스 로직

def sharings(request):
    return render(request, 'sharings.html')

def detail(request, sharing_id):
    return render(request, 'detail.html', {
        'id': sharing_id,
    })
