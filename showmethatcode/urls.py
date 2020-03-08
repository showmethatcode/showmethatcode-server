from django.contrib import admin
from django.urls import path, include
from sharings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sharings, name='sharings'),
    path('detail/<int:sharing_id>/', views.detail, name='detail'),
]
