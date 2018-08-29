from django.db import models
from Person.models import Patient
from Surgery_Details.models import Surgery
from hospital.models import PatientRoom
# Create your models here.


class Prescription(models.Model):
    pres_name = models.CharField(max_length=200)
    pres_description = models.TextField()
    pres_price = models.FloatField()

    def __str__(self):
        return self.pres_name


class Bill(models.Model):
    patient = models.ForeignKey(Patient, null =True, related_name='bill', on_delete=models.CASCADE)
    surgery = models.ForeignKey(Surgery, null=True, related_name='bill', on_delete=models.CASCADE)
    patient_room = models.ForeignKey(PatientRoom, null=True, related_name='bill', on_delete=models.CASCADE)
    prescription = models.ForeignKey(Prescription, null=True, related_name='bill', on_delete=models.CASCADE)
    bill_status = models.CharField(max_length=50)
    total = models.IntegerField(null=True)
