from django.conf.urls import url,include
from .views import UserFormView, index, LoginView, writing, CreateWriting

app_name='user_profile'
urlpatterns = [
    url(r'^register/', UserFormView.as_view(), name='register'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/$', index, name='index'),
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/(?P<pk>[0-9])/$', writing, name='writing'),
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/addnew/$', CreateWriting.as_view(), name='newriting'),
]