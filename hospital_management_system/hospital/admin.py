from django.contrib import admin
from .models import Room, PatientRoom, SurgeryRoom, Hospital

# Register your models here.
admin.register(Room)
admin.register(PatientRoom)
admin.register(SurgeryRoom)
admin.register(Hospital)
