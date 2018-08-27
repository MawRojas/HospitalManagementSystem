from django import forms
from Person.models import Doctors, Nurses, Patient

class addPatient(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['firstName', 'lastName','address','phoneNumber', 'social']
    
class addNurses(forms.ModelForm):
    class Meta:
        model=Nurses
        fields=['firstName', 'lastName','address','phoneNumber','social']

class addDoctors(forms.ModelForm):
    class Meta:
        model=Doctors
        fields=['firstName', 'lastName','address','phoneNumber','social']


class UpdatePatientDetails(forms.ModelForm):
    class Meta:
        model= Patient
        fields=['symptoms','allergies','currentMeds','docName']

class UpdateDoctors(forms.ModelForm):
    class Meta:
        model=Doctors
        fields=['shift', 'jobDesc', 'salary', 'specialty']
class UpdateNurses(forms.ModelForm):
    class Meta:
        model=Nurses
        fields=['shift', 'jobDesc', 'salary'] 