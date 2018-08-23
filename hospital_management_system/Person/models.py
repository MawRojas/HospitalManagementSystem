from django.db import models

# Create your models here.
class Persons(models.Model):
	name=models.CharField(max_length=200,default='', blank=True)
	email=models.CharField(max_length=200,default='', blank=True)
	address=models.CharField(max_length=200,default='', blank=True)
	phoneNumber=models.CharField(max_length=200,default='', blank=True)
	social=models.CharField(max_length=200,default='', blank=True)

class Patient(Persons):
	name=Persons.name
	email=Persons.email
	address=Persons.address
	phoneNumber=Persons.phoneNumber
	social=Persons.social
	symptoms=models.CharField(max_length=200,default='', blank=True)
	medications=models.CharField(max_length=200,default='', blank=True)
	allergies=models.CharField(max_length=200,default='', blank=True)	