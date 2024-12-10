from django.shortcuts import render,redirect
from django.views import View
from . forms import LoginForm,RegisterForm
from django.contrib.auth import logout,login,authenticate
from . models import Contributor

# Create your views here.

class Register(View):
    def get(self,request):
        context = {
            'form' : RegisterForm()
        }
        return render(request,'accounts/register.html',context)

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = Contributor.objects.create_user(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
                phone_number = form.cleaned_data['phone_number'],
                dob = form.cleaned_data['dob'],
                gender = form.cleaned_data['gender']
            )

            login(request,user)
            return redirect('login')
        else:
            return render(request,'accounts/register.html',{'form':RegisterForm(request.POST)})

class Login(View):
    def get(self,request):
        context = {
            'form' : LoginForm()
        }
        return render(request,'accounts/login.html',context)

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('register')
        else:
            return redirect('login')
        