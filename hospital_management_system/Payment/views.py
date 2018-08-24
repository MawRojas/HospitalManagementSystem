from django.shortcuts import render, get_object_or_404
from .models import Prescription, Bill


# Create your views here.

def prescription_list(request):
	meds = Prescription.objects.all
	return render(request, 'payment/prescription_list.html', {'meds':meds})