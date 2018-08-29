from Surgery_Details import views
from django.conf.urls import url

app_name = "Surgery_Details"

urlpatterns = [
    url('surgery_list/', views.view_surgery_details, name="Surgery_List"),
    url('equipment_details/', views.view_equipment_details, name="Equipment_Details"),
    url(r'^surgery/new/$', views.add_new_surgery_details, name='New_Surgery'),
    url(r'^equipment/new/$', views.add_new_equipment, name='New_Equipment'),
    url(r'^surgery/(?P<id>\d+)/', views.view_surgery, name='Surgery'),
    url(r'^equipment/(?P<id>\d+)/', views.view_equipment, name='Equipment'),
]
