from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.gold),
    url(r'^process$', views.process),

]