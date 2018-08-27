from django.shortcuts import render, get_object_or_404
from .models import Prescription, Bill
from .forms import AddNewPrescriptionForm, PostBill


# Create your views here.

def prescription_list(request):
    meds = Prescription.objects.all
    return render(request, 'payment/prescription_list.html', {'meds': meds})


def view_bill(request):
    bill = Bill.objects.all
    return render(request, 'payment/bill_details.html', {'bill': bill})


def add_new_prescription(request):
    if request.method == "POST":
        form = AddNewPrescriptionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'payment/prescription_list.html', {'meds': post})
        else:
            form = AddNewPrescriptionForm()
            return render(request, 'payment/add_new_prescription.html', {'form': form})


def add_new_bill(request):
    if request.method == "POST":
        form = PostBill(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'payment/bill_details.html', {'bill': post})
        else:
            form = AddNewPrescriptionForm()
            return render(request, 'payment/add_new_bill.html', {'form': form})


def view_bill_for_patient(request):
    details = get_object_or_404(Bill, patient_id=id)
    return render(request, 'payment/bill_details_patient.html', {'details': details})
