from django.db import models

# Create your models here.

class RegistrationInfo(models.Model):
	first_name=models.CharField(max_length=128)
	last_name=models.CharField(max_length=128)
	father_name=models.CharField(max_length=128)
	date_of_birth=models.DateField(max_length=40)
	roll_num=models.CharField(max_length=40,unique=True,primary_key=True,)
	email=models.EmailField(max_length=128,unique=True)
	phone=models.CharField(max_length=40)
	address=models.CharField(max_length=250)
	education=models.CharField(max_length=200)
	uid=models.CharField(max_length=250)


