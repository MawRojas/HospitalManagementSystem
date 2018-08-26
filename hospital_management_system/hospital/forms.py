from django import forms
from .models import PatientRoom, SurgeryRoom, Hospital


class PostPatientRoom(forms.ModelForm):
    class Meta:
        model = PatientRoom
        fields = ['room_number', 'price']


class PostSurgeryRooom(forms.ModelForm):
    class Meta:
        model = SurgeryRoom
        fields = ['room_number']


class PostHospital(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'address', 'phone_number']


class UpdatePatientRoom(forms.ModelForm):
    class Meta:
        model = PatientRoom
        fields = ['patient', 'nurse']


class UpdateSurgeryRoom(forms.ModelForm):
    class Meta:
        model = SurgeryRoom
        fields = ['surgery']    