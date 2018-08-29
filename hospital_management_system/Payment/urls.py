from django.contrib import admin
from django.urls import path
from Payment import views
from django.conf.urls import url

app_name = "Payment"

urlpatterns = [
    url('prescription_list/', views.prescription_list, name="Prescription_List"),
    url('view_bill/', views.view_bill, name="Bill Details"),
    url(r'^bill/(?P<id>\d+)/', views.view_bill_for_patient, name='Bill_Details_for_Patient'),
    url(r'^prescription/new/$', views.add_new_prescription, name='New Prescription'),
    url(r'^bill/new/$', views.add_new_bill, name='New_Bill'),
    url(r'^medicine/(?P<id>\d+)/', views.view_medicine, name='View_Medicine'),
    url(r'^patient/$', views.patient_name, name='View_Bill'),
]
