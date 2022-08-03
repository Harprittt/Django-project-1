from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer
from django.contrib import messages
from . models import Customer



# Create your views here.



def signup(request):
	if request.method=='POST':
		customer_id=request.POST['customer_id']
		username=request.POST['username']
		lastname=request.POST['lastname']
		firstname=request.POST['firstname']
		email=request.POST['email']
		password=request.POST['password']
		image=request.FILES['image']


		x=Customer(username=username, lastname=lastname, firstname=firstname, email=email, password=password,image=image,customer_id=customer_id)
		if form.is_valid():
			x.save()
		messages.success(request,'Your account ha been created successfully')
		

	return render(request,'customer/register.html',{})
		



def display_form(request):
	obj = Customer.objects.all()
	return render(request,'customer/display.html',{'obj': obj})



def edit(request):
	obj = Customer.objects.get()	
	return render(request,'customer/edit.html',{'obj': obj} )







def logup(request):
	return render(request,'customer/account.html',{})



    