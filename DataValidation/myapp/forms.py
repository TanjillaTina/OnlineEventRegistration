from django import forms
from django.core import validators
from myapp.models import RegistrationInfo
from django.contrib.auth.models import User
import datetime
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
import re

class SaveRegister(forms.ModelForm):
	class Meta:
		model = RegistrationInfo
		fields=['first_name','last_name','father_name','roll_num',
		'date_of_birth','phone','address','email','education']


	def clean_date_of_birth(self):
		date_of_birth = self.cleaned_data['date_of_birth']
		age = relativedelta(datetime.date.today(), date_of_birth).years
		if age < 18:
			raise ValidationError("Sorry!! You are under 18")
		return date_of_birth

	def clean_roll_num(self):
		roll_num = self.cleaned_data['roll_num']

		if RegistrationInfo.objects.filter(roll_num=roll_num).count() > 0:
			raise ValidationError("Used Roll!!! You have submitted form before with this roll number")

		elif not re.search("54", roll_num) or re.search("67", roll_num) and len(roll_num)>=6:
			raise ValidationError("Invalid Roll!!! Must be a CSE roll number")
		return roll_num

	def clean_email(self):
		pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"   
		email = self.cleaned_data['email']
		if RegistrationInfo.objects.filter(email=email).count() > 0:
			raise ValidationError("Used Email!!! You have submitted form before with this email")
		elif not re.match(pattern,email):
			raise ValidationError("Invalid Email!!! This is not a valid email")

		return email
	def clean_phone(self):
		phone = self.cleaned_data['phone']
		if RegistrationInfo.objects.filter(phone=phone).count() > 0:
			raise ValidationError("Already registered with that phone number")
		return phone

	


class AdminForm(forms.Form):
	name=forms.CharField()
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)

