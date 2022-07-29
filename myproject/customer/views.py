from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer
from django.contrib import messages



# Create your views here.



def signup(request):
	if request.method=='POST':
		username=request.POST['username']
		lastname=request.POST['lastname']
		firstname=request.POST['firstname']
		email=request.POST['email']
		password=request.POST['password']
		image=request.FILES['image']


		x=Customer(username=username, lastname=lastname, firstname=firstname, email=email, password=password,image=image)
		x.save()
		messages.success(request,'Your account ha been created successfully')
		

	return render(request,'customer/register.html',{})
		


def logup(request):
	return render(request,'customer/account.html',{})



    