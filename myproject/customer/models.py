from django.db import models

# Create your models here.


class Customer(models.Model):
	firstname = models.CharField(max_length=10, null=False, blank=False)
	lastname = models.CharField(max_length=10, null=False, blank=False)
	email = models.CharField(max_length=20, null=False,blank=False)
	username = models.CharField(max_length=20, null=False)
	password = models.CharField(max_length=10,null=False)
	image = models.ImageField(null=True,upload_to='images/')
	

	def __str__(self):
		return self.username