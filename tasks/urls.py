from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.task_list, name='task_list'),
    url(r'^create/$', views.task_create, name='task_create'),
    url(r'^(?P<id>\d+)/delete/$', views.task_delete, name='task_delete')
]