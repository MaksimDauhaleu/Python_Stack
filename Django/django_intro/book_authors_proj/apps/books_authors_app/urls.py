from django.conf.urls import url
from . import views
                    

urlpatterns = [
    url(r'^$', views.page),
    url(r'^book_info/(?P<id>\d+)$',views.book_info),
    url(r'^add_author/(?P<id>\d+)$',views.add_author),
]
