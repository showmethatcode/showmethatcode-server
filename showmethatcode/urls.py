from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.contrib import admin
from showmethatcode import settings
from showmethatcode.views import account
from sharings import views

urlpatterns = [
    path('admin/', admin.site.urls, name='administrator'),
    path('', include('social_django.urls', namespace='social')),
    # path('', views_main.index, name='index'),
    path(
        'logout/',
        LogoutView.as_view(template_name=settings.LOGOUT_REDIRECT_URL),
        name='logout'
        ),
    path('account/', account, name='account'),
    path('', views.home, name='sharings'),
    path('write/', views.write, name='write'),
    path('detail/<int:sharing_id>/', views.detail, name='detail'),
    path('detail/', views.detail_temp),
]
