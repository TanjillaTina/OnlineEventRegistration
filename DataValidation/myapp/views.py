from django.shortcuts import render
from myapp import forms
from myapp.forms import SaveRegister
from myapp.models import RegistrationInfo
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import uuid
from django.contrib import messages
import django
from django.conf import settings
from django.core.mail import send_mail

def index(request):
	form=SaveRegister()
	po=RegistrationInfo()
	if request.method=='POST':
		form=SaveRegister(request.POST)

		#form=SaveRegistartionInfo(request.POST)

		if form.is_valid():
			form.save(commit=False)
			
			fname=form.cleaned_data['first_name']
			lname=form.cleaned_data['last_name']
			faname=form.cleaned_data['father_name']
			roll=form.cleaned_data['roll_num']
			birth=form.cleaned_data['date_of_birth']
			phhn=form.cleaned_data['phone']
			addrs=form.cleaned_data['address']
			mailid=form.cleaned_data['email']
			edu=form.cleaned_data['education']
			unik=uniquess_key()
			po=RegistrationInfo(first_name=fname,last_name=lname,father_name=faname,date_of_birth=birth,roll_num=roll,email=mailid,phone=phhn,address=addrs,education=edu,uid=unik)
			po.save()
			messages.success(request, 'Form submission successful!! Plz check email for id ')
			email_body = 'Your Registration ID Number is ' + unik
			#email = EmailMessage('Congratulations!!', email_body, to=[mailid, ])
			#email.send()
			send_mail('Confirmation Mail', email_body, settings.EMAIL_HOST_USER,
				[mailid], fail_silently=False)




			return HttpResponseRedirect(reverse('index'))
			#return HttpResponseRedirect(reverse('index'))







			#print("Congrast")

		else:
			messages.error(request, form.errors)
			return HttpResponseRedirect(reverse('index'))
	return render(request,'regiform.html',{'form':form,})

def uniquess_key():
	return uuid.uuid4().hex[:15].upper()




def login(request):
	form=forms.AdminForm()
	if request.method=='POST':
		form=forms.AdminForm(request.POST)
		if form.is_valid():
			print("Validation Succes")
			name=form.cleaned_data['name']
			password=form.cleaned_data['password']
			if password=='admintest' and name=='admin':
				print("jgjjjhgjg")
				RegisteredStudentlist=RegistrationInfo.objects.order_by('roll_num')
				students={'students':RegisteredStudentlist}

				return render(request,'adminHome.html',context=students)

			 

         


	return render(request,'login.html',{'form':form})
