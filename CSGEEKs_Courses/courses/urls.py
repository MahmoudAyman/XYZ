from django.conf.urls import url

from . import views

app_name = "courses"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<course_id>[0-9]+)/$', views.getCourseAbout, name="about"),
    url(r'^form/$', views.form, name="form"),
    url(r'^login/$', views.logIn, name="login"),
    url(r'^signup/$', views.signUp, name="signup"),
    url(r'^logout/$', views.logOut, name="logout"),
    url(r'^(?P<course_id>[0-9]+)/comment/', views.postComment, name="comment"),
    url(r'^dashboard/$', views.getDashboard, name="dashboard"),
    url(r'^(?P<course_id>[0-9]+)/$', views.getCourseAbout, name="about"),

]