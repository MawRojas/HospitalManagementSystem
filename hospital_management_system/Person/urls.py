from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views
from Person.models import Persons, Patient, Employee, Doctors
urlpatterns = [
	url(r'^Person', views.addPersons, name='person'),
	url(r'^Employee', views.addEmployee,name='person'),
    url(r'^enter_details/patient/(?P<id>\d+)$', views.addPatients, name='patient_details'),
	url(r'^enter_details/doctor/$', views.addDoctor, name='doctor_details'),
	url(r'^enter_details/nurse/(?P<id>\d+)$', views.addNurse, name='nurse_details'),	
]

