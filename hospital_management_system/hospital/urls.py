
from django.conf.urls import url
from . import views

app_name = 'hospital'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^rooms/$', views.rooms_list, name='rooms'),
    url(r'^post/room/patient/$', views.post_patient_room, name='post_patient_room'),
    url(r'^post/room/surgery/$', views.post_surgery_room, name='post_surgery_room'),
    url(r'^post/hospital/$', views.post_hospital, name='post_hospital'),
    url(r'^check_in/patient/(?P<id>\d+)$', views.check_patient_in_room, name='patient_check_in'),
    url(r'^check_out/patient/(?P<id>\d+)$', views.check_patient_out_room, name='patient_check_out'),
    url(r'^book/surgery/$', views.book_surgery_room, name='book_surgery'),
    url(r'^check_out/surgery/(?P<id>\d+)$', views.checkout_surgery_room, name='check_out_surgery'),
]