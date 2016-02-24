from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^acounts', views.acounts, name='acounts'),
    # url(r'^$', views.acounts, name='acounts'),
]