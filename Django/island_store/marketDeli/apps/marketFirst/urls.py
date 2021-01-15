from django.conf.urls import url
from . import views
                    

urlpatterns = [
    url(r'^$', views.page),
    url(r'^login$', views.login),
]