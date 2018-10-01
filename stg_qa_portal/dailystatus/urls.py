from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'add/dailystatus/$', views.add_dailystatus, name='add_dailystatus'),
    url(r'edit/dailystatus/(?P<pk>[0-9]+)/$', views.edit_dailystatus, name='edit_dailystatus'),
    url(r'delete/dailystatus/(?P<pk>[0-9]+)/$', views.delete_dailystatus, name='delete_dailystatus'),
]