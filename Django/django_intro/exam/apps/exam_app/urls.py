from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^user_login$', views.user_login),
    url(r'^regist$', views.regist),
    url(r'^success$', views.success),
    url(r'^logout', views.logout),
    #######
    url(r'^add_trip$', views.add_trip),
    url(r'^create/(?P<id>\d+)$', views.create),
    url(r'^read/(?P<id>\d+)$',views.read),
    url(r'^read/(?P<id>\d+)/edit$',views.edit),
    url(r'^read/(?P<id>\d+)/update$',views.update),
    url(r'^read/(?P<id>\d+)/delete$',views.delete),
]   
