from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$',views.new),
    url(r'^book_info/(?P<id>\d+)$',views.book_info),
    url(r'^add_author/(?P<id>\d+)$',views.add_author),
    url(r'^authors$',views.authors),
    url(r'^mew$',views.mew),
    url(r'^author_info/(?P<id>\d+)$',views.author_info),
    url(r'^add_book/(?P<id>\d+)$',views.add_book),
]