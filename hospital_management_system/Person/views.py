from django.shortcuts import render, get_object_or_404, redirect
from Person.models import Persons, Patient, Employee, Doctors
from hospital.models import Hospital, PatientRoom, SurgeryRoom
from .forms import addPatient, addNurses, addDoctors, UpdatePatientDetails, UpdateDoctors, UpdateNurses
# Create your views here.

def addPersons(request):
	addPerson=Persons.objects.all()

def listPatients(request):
	patientList=Persons.patientList.all()
	print(patientList)
	return render(request, 'listpatients.html', {'patientList':patientList})



def postPatients(request):
	hospital=get_object_or_404(Hospital, id=1)
	form=addPatient(request.POST)
	if form.is_valid():
		item=form.save(commit=False)
		item.save()
		hospital.patient_rooms.add(item)
		return redirect('hospital:rooms')
	else:
		form=addPatient()
		return render(request, 'post_element.html', {'form':form, 'button_title':'Post Patient'})


def addEmployee(request):
	addEmployees=Persons.objects.all()




def postDoctors(request):	
	instance=get_object_or_404(Doctors, id=1)
	form=addDoctors(request.POST)
	if form.is_valid():
		item=form.save(commit=False)
		item.save()
		hospital.doctors.add(item)
		return redirect('hospital:rooms')
	else:
		form=addDoctors()
		return render(request, 'post_element.html', {'form':form, 'button_title':'Post Doctors'})
		
def postNurse(request):
	hospital=get_object_or_404(Nurses, id =1)
	form=addNurses(request.POST)
	if form.is_valid():
		item=form.save(commit=False)
		item.save()
		hospital.nurses.add(item)
		return render('Employee:Doctor')
	else:
		form=addNurses()
		return render(request, 'post_element.html', {'form':form, 'button_title':'Post Nurses'})

