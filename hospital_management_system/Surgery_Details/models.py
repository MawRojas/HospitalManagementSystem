from django.db import models
<<<<<<< HEAD
from hospital.models import SurgeryRoom
from Person.models import Doctors, Nurses, Patient

=======
from Person.models import Doctors, Nurses, Patient
# from django.utils import timezone
>>>>>>> master
# Create your models here.


class Surgery(models.Model):
    surgery_description = models.TextField()
    start_time = models.DateTimeField(blank=True, null=True)
    duration = models.PositiveIntegerField()
    surgery_price = models.FloatField()
    doctor_incharge = models.ForeignKey(Doctors, null=True, related_name = 'surgery', on_delete=models.CASCADE)
    nurse_incharge = models.ForeignKey(Nurses, null=True, related_name = 'surgery', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, null=True, related_name = 'surgery', on_delete=models.CASCADE)
<<<<<<< HEAD
    surgery_room = models.ForeignKey(SurgeryRoom, null=True, related_name = 'surgery', on_delete=models.CASCADE)
=======
    # surgery_room = models.ForeignKey(SurgeryRoom, null=True, related_name = 'surgery', on_delete=models.CASCADE)

    def __str__(self):
        return self.surgery_description
>>>>>>> master


class Equipment(models.Model):
    equip_name = models.CharField(max_length=200)
    equip_description = models.TextField()
    equip_price = models.FloatField()
