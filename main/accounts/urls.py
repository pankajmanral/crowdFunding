from django.urls import path
from . import views

urlpatterns = [

    path('login-page/',views.Login.as_view(),name='login'),
    path('register-page/',views.Register.as_view(),name='register')

]