from django.shortcuts import render
from person.models import Persons, Patient, Employee, Doctors
# Create your views here.

def addPersons(request):
	addPerson=Persons.objects.all()
def addPatients(request):
	addPatient=Patient.objects.all()
def addEmployee(request):
	addEmployees=Persons.objects.all()
def addDoctor(request):
	addDoctor=Employee.objects.all()
#def addNurse(request):
#	addNurse=Employee.objects.all()