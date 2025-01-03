from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import  *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient_name', 'patient_email', 'appointment_date', 'appointment_time', 'reason']
        labels = {
            'doctor': 'Doctor',
            'patient_name': 'Patient Name',
            'patient_email': 'Patient Email',
            'appointment_date': 'Date',
            'appointment_time': 'Time',
            'reason': 'Reason',
        }
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))


class modelfor(forms.ModelForm):
    class Meta:
        model=doctors
        fields='__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title','Patient_name', 'image']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'image']