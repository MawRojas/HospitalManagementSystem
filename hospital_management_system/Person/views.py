from django.shortcuts import render, get_object_or_404, redirect
from Person.models import Persons, Patient, Employee, Doctors
from hospital.models import Hospital, PatientRoom, SurgeryRoom
# Create your views here.

def addPersons(request):
    return render(request, 'templates/base.html')
def addPatients(request):
	addPatient=Patient.objects.all()
def addEmployee(request):
	addEmployees=Persons.objects.all()
def addDoctor(request):
	addDoctor=Employee.objects.all()
def addNurse(request):
	addNurse=Employee.objects.all()