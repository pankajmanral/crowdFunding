from django import forms
from django.forms import ModelForm
from . models import Contributor

class LoginForm(ModelForm):
    class Meta:
        model = Contributor
        fields = ['username','password'] 
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder' : 'Enter username','class':'border border-gray-200 border-2 rounded-md h-10 w-full px-3 '}),
            'password' : forms.PasswordInput(attrs={'placeholder' : 'Enter password','class':'border border-gray-200 border-2 rounded-md h-10 w-full px-3 '}),
        }

class RegisterForm(ModelForm):
    class Meta:
        model = Contributor
        fields = ['first_name','last_name','username','email','password','gender','phone_number','dob']
        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholder':'Enter first name','class':'border border-gray-200 border-2 rounded-md h-10 w-full px-3 '}),
            'last_name' : forms.TextInput(attrs={'placeholder':'Enter last name','class':'border border-gray-200 border-2 rounded-md h-10 w-full px-3 '}),
            'username' : forms.TextInput(attrs={'placeholder':'Enter username','class':'border border-gray-200 border-2 rounded-md h-10 w-full px-3 '}),
            'email' : forms.TextInput(attrs={'placeholder':'Enter email','class':'border border-gray-200 border-2 rounded-md h-10 w-full px-3 '}),
            'password' : forms.PasswordInput(attrs={'placeholder':'Enter password','class':'border border-gray-200 border-2 rounded-md h-10 w-full px-3 '}),
            'phone_number' : forms.NumberInput(attrs={'placeholder':'Enter phone Number','class':'border border-gray-200 border-2 rounded-md h-10 w-full px-3 '}),
            'dob' : forms.DateInput(attrs={'placeholder':'Enter date','class':'border border-gray-200 border-2 rounded-md h-10 w-full px-3 '}),
        }