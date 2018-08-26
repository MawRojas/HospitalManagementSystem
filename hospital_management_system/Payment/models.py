from django.db import models
from Person.models import Patient
from Surgery_Details.models import Surgery
# Create your models here.


class Prescription(models.Model):
	pres_name = models.CharField(max_length=200)
	pres_description = models.TextField()
	pres_price = models.FloatField()
	
	def __str__(self):
		return self.name

		
class Bill(Prescription):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	total = models.IntegerField()
	surgery = models.ForeignKey(Surgery, on_delete=models.CASCADE)
	# ##product = models.ForeignKey(Product, null =True, related_name='brands', on_delete=models.CASCADE)