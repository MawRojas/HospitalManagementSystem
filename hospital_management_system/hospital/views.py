from django.shortcuts import render, get_object_or_404, redirect
from .models import Hospital
from .forms import PostPatientRoom, PostHospital, PostSurgeryRooom


# Create your views here.
def home(request):
    return render(request, 'hospital/base.html')


def rooms_list(request):
    patient_rooms = Hospital.patient_rooms__set.all()
    surgery_rooms = Hospital.surgery_rooms__set.all()
    return redirect(request, 'hospital/list_all_rooms.html',
                    {'surgery_rooms': surgery_rooms, 'patient_rooms': patient_rooms})


def post_hospital(request):
    if request.method == 'POST':
        form = PostHospital(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('hospital:rooms')
    else:
        form = PostHospital()
    return render(request, 'hospital\post_element.html', {'form': form, 'button_title': 'Post Hospital'})


def post_patient_room(request):
    if request.method == 'POST':
        form = PostPatientRoom(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('hospital:rooms')
    else:
        form = PostPatientRoom()
    return render(request, 'hospital\post_element.html', {'form': form, 'button_title': 'Post Patient Room'})

