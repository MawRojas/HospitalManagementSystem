from django.shortcuts import render
from .models import Surgery, Equipment
# Create your views here.

def view_surgery_details(request):
	sur = Surgery.objects.all
	return render(request, 'surgery_details/surgery_details.html', {'sur':sur})

def view_equipment_details(request):
	equip = Equipment.objects.all
	return render(request, 'surgery_details/equipment_details.html', {'equip':equip})
