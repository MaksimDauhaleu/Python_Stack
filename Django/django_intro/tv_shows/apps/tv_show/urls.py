from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show$', views.create),
    url(r'^add_show$', views.add_show),
    url(r'^show/(?P<id>\d+)$',views.read),
    url(r'^show/(?P<id>\d+)/update$',views.update),
    url(r'^show/(?P<id>\d+)/edit$', views.edit),
    url(r'^(?P<id>\d+)/destroy$', views.delete),
    url(r'^show/(?P<id>\d+)/destroy$', views.delete),
    
]