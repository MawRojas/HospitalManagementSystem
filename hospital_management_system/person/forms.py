from django import forms
from django.forms import ModelForm
from .models import Persons, Employee, Doctors, Patient, Nurses

class PatientForm:
	fields=['firstName', 'lastName', 'address', 'email', 'firstName', 'firstName',] 
