from django.contrib import admin
from .models import Prescription, Bill

# Register your models here.
admin.register(Prescription)
admin.register(Bill)