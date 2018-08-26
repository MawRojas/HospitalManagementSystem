from django.db import models
from decimal import Decimal
# Create your models here.


# Create your models here.

class Persons(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    social = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Employee(Persons):
    shift = models.CharField(max_length=200, default='', blank=True)
    jobDesc = models.CharField(max_length=200, default='', blank=True)
    salary = models.DecimalField(max_digits=7, decimal_places=0, default=Decimal('0.00'))

    class Meta:
        abstract=True


class Doctors(Employee):
    specialty = models.CharField(max_length=200, default='', blank=True)
    # surgeries = models.ManyToManyField(Surgery, symmetrical=False, null=True)
    # surgery=models.ForeignKey() #total number of surgeries for particular doctor


class Nurses(Employee):
    specialty = models.CharField(max_length=200, default='', blank=True)
    # patient_rooms = models.ManyToManyField(PatientRoom, symmetrical=False, null=True)


class Patient(Persons):
    symptoms = models.CharField(max_length=200, default='', blank=True)
    allergies = models.CharField(max_length=200, default='', blank=True)
    currentMeds = models.CharField(max_length=200, default='', blank=True)
    docName = models.ForeignKey(Doctors, on_delete=models.CASCADE, default='1')

