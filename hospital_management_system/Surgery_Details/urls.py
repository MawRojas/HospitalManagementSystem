from Surgery_Details import views
from django.conf.urls import url

app_name = "Surgery_Details"

urlpatterns = [
    url('surgery_details/', views.view_surgery_details, name="Surgery_List"),
    url('equipment_details/', views.view_equipment_details, name="Equipment_Details"),
    url(r'^surgery_details/new/$', views.add_new_surgery_details, name='New Surgery Details'),
    url(r'^equipment/new/$', views.add_new_equipment, name='New Equipment'),
]
