from django.conf.urls import url

from . import views

name_space = "courses"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
]