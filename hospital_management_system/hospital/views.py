from django.shortcuts import render
from .models import Hospital


# Create your views here.
def home(request):
    return render(request, 'hospital/base.html')


def rooms_list(request):
    patient_rooms = Hospital.patient_rooms__set.all()
    surgery_rooms = Hospital.surgery_rooms__set.all()
    return request(request, 'hospital/list_all_rooms.html',
                   {'surgery_rooms': surgery_rooms, 'patient_rooms': patient_rooms})

