from django.db import models
from Person.models import Doctors, Nurses, Patient
# from app_five import Surgery, Equipment


class Room(models.Model):
    room_number = models.BigIntegerField(default=0)
    is_occupied = models.BooleanField(default='0')

    class Meta:
        abstract = True


class PatientRoom(Room):
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient')
    nurse = models.ForeignKey(Nurses, on_delete=models.CASCADE, related_name='nurse')


class SurgeryRoom(Room):
    # equipment = models.ManyToManyField(Equipment, symmetrical=False)
    # surgery = models.ForeignKey(Surgery, on_delete=models.CASCADE, related_name='surgery')
    pass


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    patient_rooms = models.ManyToManyField(PatientRoom, symmetrical=False)
    surgery_rooms = models.ManyToManyField(SurgeryRoom, symmetrical=False)
    patients = models.ManyToManyField(Patient, symmetrical=False)
    doctors = models.ManyToManyField(Doctors, symmetrical=False)
    nurses = models.ManyToManyField(Nurses, symmetrical=False)

    def save(self, *args, **kwargs):
        if Hospital.objects.count() == 1:
            raise PermissionError("Only one Hospital is allowed")

        super(Hospital, self).save(*args, **kwargs)
