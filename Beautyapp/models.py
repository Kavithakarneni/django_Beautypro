from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Upd(models.Model):
	g = [('M',"Male"),('F',"Female")]
	age = models.IntegerField(default=18)
	gender = models.CharField(max_length=7,choices=g)
	im = models.ImageField(upload_to="Profile_pics/",default="profile.jpeg")
	p = models.OneToOneField(User,on_delete=models.CASCADE)

class Book_status(models.Model):
	status=models.CharField(max_length=18,null=True)
	def __str__(self):
		return self.status

class Booking_paid(models.Model):
	paid=models.CharField(max_length=18,null=True)
	def __str__(self):
		return self.paid


class Addser(models.Model):
	s_name= models.TextField()
	s_img=models.ImageField(upload_to="images/")
	s_cost = models.IntegerField()
	def __str__(self):
		return self.s_name
	
class Sbook(models.Model):
	s = [('Charcoal facial',"charcoal facial"),('Fruit facial',"fruit facial"),('Deluxe manicure',"deluxe manicure"),('Deluxe pedicure',"deluxe pedicure"),('Facial massage',"facial massage"),('O3 facial',"o3 facial"),('Loreal hair colour',"loreal hair colour")]
	services = models.ForeignKey(Addser,on_delete=models.CASCADE,null=True)
	slot_date =models.DateField()
	slot_time =models.TimeField()
	user_id = models.IntegerField(null=True)
	status = models.ForeignKey(Book_status,on_delete=models.CASCADE,null=True)
	paid = models.ForeignKey(Booking_paid,on_delete=models.CASCADE,null=True)
	



		
		
	
		