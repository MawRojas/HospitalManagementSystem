from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views
from Person.models import Persons, Patient, Employee, Doctors
urlpatterns = [
	url(r'^Person', views.addPersons, name='person'),
	url(r'^Employee', views.addEmployee,name='person'),
	url(r'^patients/$',views.listPatients, name='patient_list'),
    url(r'^enter_details/patient/$', views.postPatients, name='patient_details'),
	url(r'^enter_details/doctor/$', views.postDoctors, name='doctor_details'),
	url(r'^enter_details/nurse/$', views.postNurse, name='nurse_details'),	
	
]

