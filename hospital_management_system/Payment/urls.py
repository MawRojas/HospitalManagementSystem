from django.contrib import admin
from django.urls import path
from Payment import views
from django.conf.urls import url

app_name="Payment"

urlpatterns = [
	url('prescription_list/', views.prescription_list, name="Prescription List"),
	url('view_bill/', views.view_bill, name="Bill Details"),
]
