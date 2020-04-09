from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')

def account(request):
    return redirect('/login/google-oauth2')
