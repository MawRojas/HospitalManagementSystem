from django.contrib import admin
from django.urls import path
from Surgery_Details import views
from django.conf.urls import url

app_name = "Surgery_Details"

urlpatterns = [
	url('surgery_details/', views.view_surgery_details, name="Surgery_List"),
	url('equipment_details/', views.view_equipment_details, name="Equipment_Details"),
]
