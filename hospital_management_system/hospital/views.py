from django.shortcuts import render, get_object_or_404, redirect
from .models import Hospital, PatientRoom, SurgeryRoom
from .forms import PostPatientRoom, PostHospital, PostSurgeryRooom, UpdatePatientRoom, UpdateSurgeryRoom
from datetime import datetime


# Create your views here.
def home(request):
    return render(request, 'hospital/base.html')


def rooms_list(request):
    hospital = get_object_or_404(Hospital, id=1)
    patient_rooms = hospital.patient_rooms.all()
    surgery_rooms = hospital.surgery_rooms.all()
    print(patient_rooms)
    return render(request, 'hospital/list_all_rooms.html',
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
    hospital = get_object_or_404(Hospital, id=1)
    if request.method == 'POST':
        form = PostPatientRoom(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            hospital.patient_rooms.add(item)
            return redirect('hospital:rooms')
    else:
        form = PostPatientRoom()
    return render(request, 'hospital\post_element.html', {'form': form, 'button_title': 'Post Patient Room'})


def post_surgery_room(request):
    hospital = get_object_or_404(Hospital, id=1)
    if request.method == 'POST':
        form = PostSurgeryRooom(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            hospital.surgery_rooms.add(item)
            return redirect('hospital:rooms')
    else:
        form = PostSurgeryRooom()
    return render(request, 'hospital\post_element.html', {'form': form, 'button_title': 'Post Surgery Room'})


def check_patient_in_room(request, id):
    instance = get_object_or_404(PatientRoom, id=id)
    form = UpdatePatientRoom(request.POST, instance=instance)
    if form.is_valid():
        item = form.save(commit=False)
        item.is_occupied = '1'
        item.save()
        return redirect('hospital:rooms')
    else:
        form = UpdatePatientRoom()
    return render(request, 'hospital\post_element.html', {'form': form, 'button_title': 'Check Patient In'})


def check_patient_out_room(request, id):
    instance = get_object_or_404(PatientRoom, id=id)
    instance.is_occupied = '0'
    instance.nurse_id = None
    instance.patient_id = None
    instance.save()
    return redirect('hospital:rooms')


def book_surgery_room(request):
    instance = get_object_or_404(SurgeryRoom, is_occupied='0')
    form = UpdateSurgeryRoom(request.POST, instance=instance)
    if form.is_valid():
        item = form.save(commit=False)
        item.is_occupied = '1'
        item.save()
        return redirect('hospital:rooms')
    else:
        form = UpdateSurgeryRoom()
    return render(request, 'hospital\post_element.html', {'form': form, 'button_title': 'Book Surgery Room'})


def checkout_surgery_room(request, id):
    instance = get_object_or_404(SurgeryRoom, id=id)
    instance.is_occupied = '0'
    instance.surgery_id = None
    instance.save()
    return redirect('hospital:rooms')


def display_surgery_schedule(request):
    hospital = get_object_or_404(Hospital, id=1)
    datetime_now = datetime.now()
    surgery_rooms_booked = hospital.surgery_rooms.all().filter(is_occupied='1').order_by('surgery__start_time')
    surgery_rooms_free = hospital.surgery_rooms.all().filter(is_occupied='0').order_by('surgery__start_time')
    return render(request, 'hospital\surgery_schedule.html', {'booked': surgery_rooms_booked,
                                                              'free': surgery_rooms_free,
                                                              'time': datetime_now})




