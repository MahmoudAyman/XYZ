from django.conf.urls import url

from . import views

app_name = "courses"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<course_id>[0-9]+)/$', views.getCourseAbout, name='about'),
    url(r'^form/$', views.form, name="form"),
    url(r'^login/$', views.logIn, name="login"),
    url(r'^signup/$', views.signUp, name="signup"),
]