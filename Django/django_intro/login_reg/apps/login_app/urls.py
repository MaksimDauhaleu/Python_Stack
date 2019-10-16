from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^user_login$', views.user_login),
    url(r'^regist$', views.regist),
    url(r'^add_user$', views.add_user),
    url(r'^success$', views.success),
]