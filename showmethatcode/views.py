from django.shortcuts import render

def account(request):
    if not Group.objects.filter(name='showmethatcode').exists():
        Group.objects.create(name='showmethatcode')
    return render(request, 'account.html')
