from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views
from Person.models import Persons, Patient
urlpatterns = [
	url(r'Person', views.personList, name='Persons'),
	url(r'Patient', views.patientList, name='Person'),
	
]

