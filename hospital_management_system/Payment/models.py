from django.db import models

# Create your models here.

class Prescription(models.Model):
	pres_name = models.CharField(max_length=200)
	pres_description = models.TextField()
	pres_price = models.FloatField()
	
	def __str__(self):
		return self.name

		
class Bill(Prescription):
	# patient_id = models.ForeignKey('Patient.ID')
	total = models.IntegerField()
	# surgery_id = models.ForeignKey('Surgery.surgery_id')
	# ##product = models.ForeignKey(Product, null =True, related_name='brands', on_delete=models.CASCADE)