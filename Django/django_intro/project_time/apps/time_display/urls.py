from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.time),
    url(r'^time_display$', views.time),
]