from django.shortcuts import render, get_object_or_404
from .models import Prescription, Bill
from .forms import AddNewPrescriptionForm, PostBillForm, BillForPatient
from hospital.models import Hospital

# Create your views here.

def prescription_list(request):
    meds = Prescription.objects.all
    hospital = get_object_or_404(Hospital, id=1)
    return render(request, 'payment/prescription_list.html', {'meds': meds, 'hospital':hospital})


def view_bill(request):
    bill = Bill.objects.all
    hospital = get_object_or_404(Hospital, id=1)
    return render(request, 'payment/bill_details.html', {'bill': bill, 'hospital':hospital})


def add_new_prescription(request):
    if request.method == "POST":
        form = AddNewPrescriptionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'payment/prescription_display.html', {'meds': post})
    else:
        form = AddNewPrescriptionForm()
    return render(request, 'payment/add_new_prescription.html', {'form': form})


def add_new_bill(request):
    if request.method == "POST":
        form = PostBillForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'payment/bill_display.html', {'bill': post})
    else:
        form = PostBillForm()
    return render(request, 'payment/add_new_bill.html', {'form': form})

def patient_name(request):
    if request.method == "POST":
        form = BillForPatient(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'payment/bill_display.html', {'bill': post})
    else:
        form = BillForPatient()
    return render(request, 'payment/input_patient.html', {'form': form})


def view_bill_for_patient(request, id):
    details = get_object_or_404(Bill, patient=id)
    hospital = get_object_or_404(Hospital, id=1)
    total = float(details.surgery.surgery_price) + float(details.patient_room.price) + float(details.prescription.pres_price)
    return render(request, 'payment/bill_display.html', {'bill': details, 'hospital':hospital, 'total': total})


def view_medicine(request, id):
    details = get_object_or_404(Prescription, id=id)
    hospital = get_object_or_404(Hospital, id=1)
    return render(request, 'payment/prescription_display.html', {'meds': details, 'hospital':hospital})