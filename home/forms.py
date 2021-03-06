from django.contrib.auth import get_user_model
User = get_user_model()
from django import forms

from allauth.account.forms import SignupForm

class MyCustomSignupForm(SignupForm):
	class Meta:
		model = User
		fields = ('username','school_name','email','mobile','city','district','state','country','pin_code')



from django.contrib.auth.forms import UserCreationForm



class UserSignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username','school_name','email','mobile','city','district','state','country','pin_code')
