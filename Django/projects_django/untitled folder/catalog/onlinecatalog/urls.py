from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^about$', views.about, name='about'),
    url(r'^login$', views.login, name='login'),
    url(r'^user_login$', views.user_login, name='user_login'),
    url(r'^regist$', views.regist, name='regist'),
    url(r'^price_range$', views.price_range, name='price_range'),
    url(r'^regist_process$', views.regist_process, name='regist_process'),
    url(r'^(?P<sneaker_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^cart/(?P<sneaker_id>[0-9]+)/$', views.add_to_cart, name='cart'),
    url(r'^cart/$', views.cart, name='main_cart'),
    url(r'^checkout/$', views.checkout, name='checkout'),
]

