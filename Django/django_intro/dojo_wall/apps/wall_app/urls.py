from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^user_login$', views.user_login),
    url(r'^regist$', views.regist),
    url(r'^success$', views.success),
    url(r'^logout', views.logout),
    url(r'^message', views.post_message),
    url(r'^comment', views.add_comment),
    url(r'^delete', views.delete),
]