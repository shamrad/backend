from django.conf.urls import url,include
from . import views

app_name='user_profile'
urlpatterns = [
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/$', views.index, name='index'),
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/(?P<pk>[0-9])/$', views.writing, name='writing'),
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/(?P<pk>[0-9])/delete/$', views.WritingDelete.as_view(), name='writing-dlt'),


    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/addnew/$', views.CreateWriting.as_view(), name='newriting'),
    # pk inja baraye membre
    url(r'^(?P<pk>[0-9])/edit/$', views.EditStu.as_view(), name='edit'),
    url(r'^$', views.CreateStu.as_view(), name='newstu'),

]