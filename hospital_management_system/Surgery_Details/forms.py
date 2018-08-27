from django import forms
from .models import Surgery, Equipment


class PostSurgeryDetailsForm(forms.ModelForm):
    class Meta:
        model = Surgery
        fields = ('surgery_description', 'start_time', 'duration', 'surgery_price', 'doctor_incharge', 'nurse_incharge',
                  'patient', 'surgery_room')


class AddNewEquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('equip_name', 'equip_description', 'equip_price')
