from django.shortcuts import render
from Person.models import Persons, Patient, Employee, Doctors
# Create your views here.

def addPersons(request):
	addPerson=Persons.objects.all()

def addPatients(request):
	instance=get_object_or_404(Patient)
	form=UpdatePatientDetails(request.POST, instance=instance)
	if form.is_valid():
		item=form.save(commit=False)
		item.is_occupied='1'
		item.save()
		return redirect('Person:Patient')

def addEmployee(request):
	addEmployees=Persons.objects.all()
def addDoctor(request):	
	instance=get_object_or_404(Doctors)
	form=UpdateDoctors(request.POST, instance=instance)
	if form.is_valid():
		item=form.save(commit=False)
		item.is_occupied='1'
		item.save()
		return redirect('Employee:Doctor')
def addNurse(request):
	instance=get_object_or_404(Nurses)
	form=UpdateNurses(request.POST, instance=instance)
	if form.is_valid():
		item=form.save(commit=False)
		item.is_occupied='1'
		item.save()
		return redirect('Employee:Doctor')