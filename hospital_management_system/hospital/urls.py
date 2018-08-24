from django.conf.urls import url
from . import views

app_name = 'hospital'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^rooms/$', views.home, name='rooms'),
    url(r'^post/room/patient/$', views.post_patient_room, name='post_patient_room'),
    url(r'^post/hospital/$', views.post_hospital, name='post_hospital'),
]