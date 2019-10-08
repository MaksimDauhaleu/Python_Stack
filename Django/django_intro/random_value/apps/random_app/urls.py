from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.random_number),
    url(r'^name$', views.my_name),
    url(r'^reset$', views.reset),

]