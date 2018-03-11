from django import forms
from django.core import validators
from myapp.models import RegistrationInfo
from django.contrib.auth.models import User


class SaveRegister(forms.ModelForm):
	class Meta:
		model = RegistrationInfo
		fields=['first_name','last_name','father_name','roll_num',
		'date_of_birth','phone','address','email','education']

		def clean_roll(self):
			roll = self.cleaned_data['roll_num']
			if roll==27:
				raise forms.ValidationError("Enter a valid mail")
				

class AdminForm(forms.Form):
	name=forms.CharField()
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)

