from django.conf.urls import url, include # added an import!
# from django.contrib import admin              # comment out, or just delete
from . import views
urlpatterns = [
    url(r'^bears$', views.one_method),                        # would only match localhost:8000/bears
    url(r'^bears/(?P<my_val>\d+)$', views.another_method),    # would match localhost:8000/bears/23
    url(r'^bears/(?P<name>\w+)/poke$', views.yet_another),    # would match localhost:8000/bears/pooh/poke
    url(r'^(?P<id>[0-9]+)/(?P<color>\w+)$', views.one_more),  # would match localhost:8000/17/brown
]
