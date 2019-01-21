from django.conf.urls import include, url
from django.contrib import admin
from .views import home

urlpatterns = [
    url(r'^project/', include('projet.urls', namespace='project')),
    url(r'^user/', include('user.urls', namespace='user')),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'', home, name='home'),
]
