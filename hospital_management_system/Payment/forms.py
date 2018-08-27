from django import forms
from .models import Prescription, Bill


class AddNewPrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('pres_name', 'pres_description', 'pres_price')


class PostBill(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ('patient_id', 'surgery_id', 'total')
