from django import forms
from .models import Prescription, Bill


class AddNewPrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('pres_name', 'pres_description', 'pres_price')


class PostBillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ('patient', 'surgery', 'patient_room', 'prescription', 'bill_status')

class BillForPatient(forms.ModelForm):
    class Meta:
        model = Bill
        fields = (['patient'])