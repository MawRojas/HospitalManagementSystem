from django import forms
from .forms import ModelForm
from Person.models import Doctors, Nurses, Patient

class addPatient(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['firstName', 'lastName','address','email','phoneNumber','SSN']

class addNurses(forms.ModelForm):
    class Meta:
        model=Nurses
        fields=['firstName', 'lastName','address','email','phoneNumber','SSN']
class addDoctors(forms.ModelForm):
    class Meta:
        model=Doctors
        fields=['firstName', 'lastName','address','email','phoneNumber','SSN']

class UpdatePatientDetails:
    class Meta:
        model= Patient
        fields=['Symptoms','Allergies','Medications','Doctor Name']
class UpdateDoctors:
    class Meta:
        model=Doctors
        fields=['Shifts', 'Job Description', 'Salary', 'Specialty']
class UpdateNurses:
    class Meta:
        model=Nurses
        fields=['Shifts', 'Job Description', 'Salary'] 