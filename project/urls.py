from django.conf.urls import url
from project.views import add, view, index

urlpatterns = [
    url(r'^add', add, name='add'),
    url(r'^(?P<id>\d+)', view, name='view'),
    url(r'', index, name='index'),
]
