from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer



# Create your views here.



def signup(request):
	
	if request.method=='POST':
		username=request.POST['username']
		lastname=request.POST['lastname']
		firstname=request.POST['firstname']
		email=request.POST['email']
		password=request.POST['password']

		x=Customer(username=username, lastname=lastname, firstname=firstname, email=email, password=password)
		x.save()
		return HttpResponse("Your account has been created successfully")
		return redirect(request,'signup',{})
		


def logup(request):
	return render(request,'customer/account.html',{})



    