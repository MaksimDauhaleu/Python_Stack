from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^about$', views.catalog, name='about'),
    url(r'^(?P<sneaker_id>[0-9]+)/$', views.detail, name='detail'),
]

