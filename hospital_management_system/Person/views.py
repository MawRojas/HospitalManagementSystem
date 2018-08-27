from django.shortcuts import render, get_object_or_404, redirect
from Person.models import Persons, Patient, Employee, Doctors
from hospital.models import Hospital, PatientRoom, SurgeryRoom
from .forms import addPatient, addNurses, addDoctors, UpdatePatientDetails, UpdateDoctors, UpdateNurses
# Create your views here.

def addPersons(request):
	addPerson=Persons.objects.all()

def listPatients(request):
	hospital=get_object_or_404(Hospital, id=1)
	patientList=hospital.patients.all()
	print(patientList)
	return render(request, 'listpatients.html', {'patientList':patientList})


def postPatients(request):
	hospital=get_object_or_404(Hospital, id=1)
	form=addPatient(request.POST)
	if form.is_valid():
		item=form.save(commit=False)
		item.save()
		hospital.patients.add(item)
		return redirect('hospital:rooms')
	else:
		form=addPatient()
		return render(request, 'post_element.html', {'form':form, 'button_title':'Post Patient'})

def UpdatePatientDetail(request):
	hospital=get_object_or_404(Hospital, id=1)
	form=UpdatePatientDetails(request.POST)
	if form.is_valid():
		item=form.save(commit=False)
		item.save()
		hospital.patients.add(item)
		return redirect('hospital:rooms')
	else:
		form=UpdatePatientDetails()
		return render(request, 'post_element.html', {'form':form, 'button_title':'Post Patient'})


def addEmployee(request):
	addEmployees=Persons.objects.all()


def listDoctors(request):
	hospital=get_object_or_404(Hospital, id=1)
	docList=hospital.doctors.all()
	print(docList)
	return render(request, 'listdoctors.html', {'docList':docList})
 

def postDoctors(request):	
	hospital=get_object_or_404(Hospital, id=1)
	form=addDoctors(request.POST)
	if form.is_valid():
		item=form.save(commit=False)
		item.save()
		hospital.doctors.add(item)
		return redirect('hospital:rooms')
	else:
		form=addDoctors()
		return render(request, 'post_element.html', {'form':form, 'button_title':'Post Doctors'})
def updateDoc(request):
	hospital=get_object_or_404(Hospital, id=1)
	form=UpdateDoctors(request.POST)
	if form.is_valid():
		item=form.save(commit=False)
		item.save()
		hospital.doctors.add(item)
		return render('hospital:rooms')
	else:
		form=UpdateDoctors()
		return render(request, 'post_element.html', {'form':form, 'button_title':'Post Doctors'})


def listNurses(request):
	hospital=get_object_or_404(Hospital, id=1)
	nurseList=hospital.nurses.all()
	print(nurseList)
	return render(request, 'listnurses.html', {'nurseList':nurseList})


def postNurse(request):
	hospital=get_object_or_404(Hospital, id =1)
	form=addNurses(request.POST)
	if form.is_valid():
		item=form.save(commit=False)
		item.save()
		hospital.nurses.add(item)
		return redirect('hospital:rooms')
	else:
		form=addNurses()
		return render(request, 'post_element.html', {'form':form, 'button_title':'Post Nurses'})

def updateNurse(request):
	hospital=get_object_or_404(Hospital, id=1)
	form=UpdateNurses(request.POST)
	if form.is_valid():
		item=form.save(commit=False)
		item.save()
		hospital.nurses.add(item)
		return redirect('hospital:rooms')
	else:
		form=UpdateNurses()
		return render(request, 'post_element.html', {'form':form, 'button_title':'Post Nurses'})








		