from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^user_login$', views.user_login),
    url(r'^regist$', views.regist),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout', views.logout),
    url(r'^trips/new', views.create),
    url(r'^add_process', views.add_process),
    url(r'^trip/edit/(?P<id>\d+)', views.update),
    url(r'^update_process/(?P<id>\d+)', views.update_process),
    url(r'^trip/(?P<id>\d+)', views.trip_info),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]
