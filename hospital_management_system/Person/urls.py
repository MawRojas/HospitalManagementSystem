from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views
from person.models import Persons, Patient, Employee, Doctors
urlpatterns = [
	url(r'Person', views.addPersons, name='person'),
	url(r'Patient', views.addPatients, name='person'),
	url(r'Employee', views.addEmployee,name='person'),
	url(r'Doctors', views.addDoctor,name='person'),
	url(r'Nurses', views.addNurse,name='Persons'),
]

