from django.shortcuts import render,redirect
from .forms import Usreg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from . models import Upd,Addser,Sbook,Book_status,Booking_paid
from datetime import datetime,date
# Create your views here.

def home(request):
	return render(request,'Beautyapp/home.html')

def about(request):
	return render(request,'Beautyapp/about.html')

def contact(request):
	return render(request,'Beautyapp/contact.html')

def regi(request):
	m = Usreg()
	if request.method == "POST":
		m=Usreg(request.POST)
		if m.is_valid():
			e = m.save(commit=False)
			e.save()
			#print(e)
			#return HttpResponse("registered successfully")
			messages.warning(request,"Hi {} you are successfully registered".format(e.username))
			return redirect("login")
	return render(request,'Beautyapp/registration.html',{'y':m})

@login_required
def dashboard(request):
	d=Addser.objects.all()
	if request.method == "POST":
		return redirect("book")
	return render(request,'Beautyapp/dashboard.html',{"das":d})
@login_required
def booking(request):
	user=User.objects.get(id=request.user.id)
	services=Addser.objects.all()
	error=False
	if request.method == "POST":
		s=request.POST['services']
		d=request.POST['slot_date']
		t=request.POST['slot_time']
		sta=Book_status(status="Pending")
		sta.save()
		paid=Booking_paid(paid="Not paid")
		paid.save()
		serv=Addser.objects.get(s_name=s)
		serv.save()
		print(serv)
		Sbook.objects.create(paid=paid,user_id=user.id,slot_date=d,slot_time=t,services=serv,status=sta)
		error=True
		messages.success(request,"booking successfully")
		return redirect("ds")
	#d={'error':error,'servi':services}
	#d1=d['servi']
	return render(request,'Beautyapp/booking.html',{'s':services})
@login_required
def profile(request):
	#data=User.objects.get(id=id)
	return render(request,'Beautyapp/profile.html')

@login_required
def myb(request,id):
	mb=Sbook.objects.filter(user_id=id)
	return render(request,'Beautyapp/myb.html',{'bm':mb})

@login_required
def  services(request):
	services=Addser.objects.all()
	return render(request,'Beautyapp/services.html',{"li":services})

@login_required
def  ads(request):
	if request.method == "POST":
		Na=request.POST['s_name']
		Im=request.FILES['s_img']
		Co=request.POST['s_cost']
		Addser.objects.create(s_name=Na,s_img=Im,s_cost=Co)
		return redirect("ser")
	As=Addser()
	return render(request,'Beautyapp/ads.html',{"n":As})

@login_required
def  delete(request,id):
	b=Addser.objects.get(id=id)
	b.delete()
	return redirect("ser")

@login_required
def user_edit(request,id):
	edit=User.objects.get(id=id)
	if request.method=="POST":
		edit.username=request.POST.get('username')
		edit.first_name=request.POST.get('first_name')
		edit.last_name=request.POST.get('last_name')
		edit.email=request.POST.get('email')
		edit.save()
		return redirect("pro")
	return render(request,'Beautyapp/user_edit.html',{'e':edit})

@login_required
def Allus(request):
	alu=User.objects.all()
	return render(request,'Beautyapp/all_users.html',{'al':alu})
@login_required
def  Admin_delete(request,id):
	ab=User.objects.get(id=id)
	ab.delete()
	return redirect("allus")
def Admin_edit(request,id):
	ed=User.objects.get(id=id)
	if request.method=="POST":
		ed.username=request.POST.get('username')
		ed.first_name=request.POST.get('first_name')
		ed.last_name=request.POST.get('last_name')
		ed.email=request.POST.get('email')
		ed.save()
		return redirect("allus")
	return render(request,'Beautyapp/Admin_edit.html',{'de':ed})

@login_required
def  All_book(request):
	al=Sbook.objects.all()
	return render(request,'Beautyapp/All_bookings.html',{'al':al})
@login_required
def  Bdel(request,id):
	bdl=Sbook.objects.get(id=id)
	bdl.delete()
	return redirect('alb')
'''@login_required
def Eb(request,id):
	bed=Sbook.objects.get(id=id)
	if request.method=="POST":
		bed.services=request.POST.get('services')
		bed.slot_date=request.POST.get('slot_date')
		bed.slot_time=request.POST.get('slot_time')
		#bed.status=request.POST.get('status')
		#bed.paid=request.POST.get('paid')
		bed.save()
		return redirect('alb')
	return render(request,'Beautyapp/Edit_booking.html',{'bed':bed})'''
@login_required
def payment(request,id):
	pn=Sbook.objects.get(id=id)
	if request.method == "POST":
		psta=Booking_paid(paid="Paid")
		psta.save()
		pn.paid=psta
		print(pn.paid)
		pn.save()
		messages.success(request,"payment successfully")
		return redirect("ds")
	return render(request,"Beautyapp/pay.html")
@login_required
def St(request,id):
	st=Sbook.objects.get(id=id)
	sts=Book_status(status="Accepted")
	sts.save()
	st.status=sts
	st.save()
	return redirect('alb')

