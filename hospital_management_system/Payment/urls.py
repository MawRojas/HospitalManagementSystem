from django.contrib import admin
from django.urls import path
from Payment import views
from django.conf.urls import url

app_name = "Payment"

urlpatterns = [
    url('prescription_list/', views.prescription_list, name="Prescription List"),
    url('view_bill/', views.view_bill, name="Bill Details"),
    url(r'^bill/(?P<id>\d+)/', views.view_bill_for_patient, name='Bill Details for Patient'),
    url(r'^prescription/new/$', views.add_new_prescription, name='New Prescription'),
    url(r'^bill/new/$', views.add_new_bill, name='New Bill'),
]
