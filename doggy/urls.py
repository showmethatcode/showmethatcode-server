from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.intro, name='intro'),
    path('<str:doggy>/', views.result, name='result')
]
