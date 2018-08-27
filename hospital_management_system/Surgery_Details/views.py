from django.shortcuts import render
from .models import Surgery, Equipment
from .forms import PostSurgeryDetailsForm, AddNewEquipmentForm


# Create your views here.

def view_surgery_details(request):
    sur = Surgery.objects.all
    return render(request, 'surgery_details/surgery_details.html', {'sur': sur})


def view_equipment_details(request):
    equip = Equipment.objects.all
    return render(request, 'surgery_details/equipment_details.html', {'equip': equip})


def add_new_surgery_details(request):
    if request.method == "POST":
        form = PostSurgeryDetailsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'surgery_details/surgery_details.html', {'sur': post})
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
            return render(request, 'surgery_details/equipment_details.html', {'sur': post})
    else:
        form = AddNewEquipmentForm()
    return render(request, 'surgery_details/add_new_equipment.html', {'form': form})
