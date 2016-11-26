from django.conf.urls import url,include
from . import views

app_name='user_profile'
urlpatterns = [
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/$', views.index, name='index'),
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/(?P<text_id>[a-zA-Z0-9_.])/$', views.writing, name='writing'),
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/addnew/$', views.CreateWriting.as_view(), name='newriting'),
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/edit/$', views.EditStu.as_view(), name='edit'),
    url(r'^$', views.CreateStu.as_view(), name='newstu'),

]