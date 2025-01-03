from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def homepage(request):
    return HttpResponse("<h1>Welcome to your Django App!</h1>")

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment has been booked successfully!')
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
        
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def about(request):
    return render(request, 'about.html')


def doctorsinfo(request):
    if request.method=='POST':
        form=modelfor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/doctor_list')

    else:
        form=modelfor()


    return render(request, 'doctor_register.html',{'form': modelfor})

def info(request):
    object=doctors.objects.all()
    return render(request, 'doctor_list.html', {'results': object})


def update(request, pk):
    object2=doctors.objects.get(pk=pk)
    forms=modelfor(instance=object2)
    if request.method=='POST':
        forms=modelfor(request.POST, instance=object2 )
        if forms.is_valid():
            forms.save()
            return redirect('/doctor_list')
        
    return render(request, 'update.html', {'formss': forms})


def delete(request, pk):
    object3=doctors.objects.get(pk=pk)
    object3.delete()
    return redirect('/doctor_list')


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})

def update_appointment(request, pk):
    object4=Appointment.objects.get(pk=pk)
    form=AppointmentForm(instance=object4)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=object4)
        if form.is_valid():
            form.save()
            return redirect('/appointment_list')
    else:
        form = AppointmentForm(instance=object4)
    return render(request, 'appointments_update.html', {'forms': form})

def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return redirect('appointment_list')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/show')  
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def contact_detail_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contactdetail.html', {'contact': contact})

def contact_list_view(request):
    contacts = Contact.objects.all()
    return render(request, 'contactlist.html', {'contacts': contacts})


def show(request):
    return render(request, 'show.html')