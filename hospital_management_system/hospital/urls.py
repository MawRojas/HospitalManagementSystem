from django.conf.urls import url
from . import views

app_name = 'hospital'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^rooms/$', views.home, name='home'),
]