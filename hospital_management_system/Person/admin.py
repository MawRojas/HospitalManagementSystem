from django.contrib import admin
from .models import Patient, Nurses, Doctors

# Register your models here.
admin.register(Patient)
admin.register(Nurses)
admin.register(Doctors)
