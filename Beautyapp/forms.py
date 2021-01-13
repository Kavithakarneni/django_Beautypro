from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import Upd,Sbook,Addser
#from Beauty_Parlour_Management_System.settings import TIME_INPUT_FORMATS

class Usreg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Enter Password",
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Enter Confirm Password",
		}))

	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your Username",
			"required":True,}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter First Name",
			"required":True,}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Last Name",
			"required":True,}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Enter your Emailid",
			"required":True,})
		}


		

