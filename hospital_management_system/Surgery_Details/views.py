from django.shortcuts import render, get_object_or_404
from .models import Surgery, Equipment
from .forms import PostSurgeryDetailsForm, AddNewEquipmentForm
from hospital.models import Hospital


# Create your views here.

def view_surgery_details(request):
    sur = Surgery.objects.all
    hospital = get_object_or_404(Hospital, id=1)
    return render(request, 'surgery_details/surgery_details.html', {'sur': sur, 'hospital':hospital})


def view_equipment_details(request):
    equip = Equipment.objects.all
    hospital = get_object_or_404(Hospital, id=1)
    return render(request, 'surgery_details/equipment_details.html', {'equip': equip, 'hospital':hospital})


def add_new_surgery_details(request):
    if request.method == "POST":
        form = PostSurgeryDetailsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'surgery_details/surgery_display.html', {'sur': post})
    else:
        form = PostSurgeryDetailsForm()
    return render(request, 'surgery_details/add_new_surgery_details.html', {'form': form})


def add_new_equipment(request):
    if request.method == "POST":
        form = AddNewEquipmentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'surgery_details/equipment_display.html', {'equip': post})
    else:
        form = AddNewEquipmentForm()
    return render(request, 'surgery_details/add_new_equipment.html', {'form': form})


def view_surgery(request, id):
    details = get_object_or_404(Surgery, id=id)
    hospital = get_object_or_404(Hospital, id=1)
    return render(request, 'surgery_details/surgery_display.html', {'sur': details, 'hospital':hospital})


def view_equipment(request, id):
    details = get_object_or_404(Equipment, id=id)
    hospital = get_object_or_404(Hospital, id=1)
    return render(request, 'surgery_details/equipment_display.html', {'equip': details, 'hospital':hospital})
