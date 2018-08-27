from django import forms
from .models import PatientRoom, SurgeryRoom, Hospital
from Surgery_Details.models import Equipment


class PostPatientRoom(forms.ModelForm):
    class Meta:
        model = PatientRoom
        fields = ['room_number', 'price']


class PostSurgeryRooom(forms.ModelForm):
    class Meta:
        model = SurgeryRoom
        exclude = ['is_occupied', 'surgery']

    def __init__(self, *args, **kwargs):
        super(PostSurgeryRooom, self).__init__(*args, **kwargs)
        self.fields['equipment'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['equipment'].help_text = ""
        self.fields['equipment'].queryset = Equipment.objects.all()


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
