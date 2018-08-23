from django.shortcuts import render, get_object_or_404
from Person.models import Persons, Patient

# Create your views here.

def personList(request):
	persons=Persons.objects.all()
def patientList(request):
	patients=Patient.objects.all()