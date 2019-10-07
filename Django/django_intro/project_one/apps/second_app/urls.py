from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^second$', views.index),
    url(r'^second/new$', views.new),
]