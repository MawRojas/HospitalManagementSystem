from django.db import models
from Person.models import Patient
from Surgery_Details.models import Surgery
# Create your models here.


class Prescription(models.Model):
    pres_name = models.CharField(max_length=200)
    pres_description = models.TextField()
    pres_price = models.FloatField()

    def __str__(self):
        return self.pres_name


class Bill(Prescription):
    patient_id = models.ForeignKey(Patient, null =True, related_name='bill', on_delete=models.CASCADE)
    surgery_id = models.ForeignKey(Surgery, null =True, related_name='bill', on_delete=models.CASCADE)
    total = models.IntegerField()
