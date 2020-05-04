from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.contrib import admin
from showmethatcode import settings
from showmethatcode.views import account, index
from sharings.views import home, write, detail, edit_form, edit

urlpatterns = [
    path('admin/', admin.site.urls, name='administrator'),
    path('', index, name='index'),
    path('', include('social_django.urls', namespace='social')),
    path(
        'logout/',
        LogoutView.as_view(template_name=settings.LOGOUT_REDIRECT_URL),
        name='logout'
        ),
    path('account/', account, name='account'),
    path('sharings/', home, name='sharings'),
    path('write/', write, name='write'),
    path('edit/<int:sharing_id>', edit, name='edit'),
    path('sharings/<int:sharing_id>/', detail, name='detail'),
    path('sharings/edit/<int:sharing_id>/', edit_form, name='edit_form'),
    path('doggy/', include('doggy.urls')),
]
