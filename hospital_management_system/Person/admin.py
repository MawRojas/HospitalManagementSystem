from django.contrib import admin
from .models import Persons, Employee, Doctors, Nurses, Patient
# Register your models here.
admin.register(Persons)
admin.register(Employee)
admin.register(Doctors)
admin.register(Nurses)
admin.register(Patient)
