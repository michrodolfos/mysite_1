from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewDoctorForm, NewPatientForm, NewRadiologyCommandForm
from .models import FinalSchedule


# Create your views here.


def homepage(request):
    return render(request=request,
                  template_name='main/home.html')


# def register(request):
#    if request.method == 'POST':
#        form = NewDoctorForm(request.POST)
#        if form.is_valid():
#            user = form.save()
#            username = form.cleaned_data.get('username')
#            messages.success(request, f'New Account Created: {username}')
#            login(request, user)
#            messages.info(request, f'You are now logged in as: {username}')
#            return redirect('main:homepage')
#       else:
#            for msg in form.error_messages:
#                messages.error(request, f'{msg}: {form.error_messages[msg]}')
#   form = NewDoctorForm
#   return render(request,
#                  'main/register.html',
#                  context={'form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('main:homepage')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()
    return render(request,
                  'main/login.html',
                  {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('main:homepage')


def add_new_patient(request):
    if request.method == 'POST':
        form = NewPatientForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f'New Patient Added : {first_name} {last_name}')
            return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')
    form = NewPatientForm
    return render(request,
                  'main/add-patient.html',
                  context={'form': form})


def make_radiology_command(request):
    if request.method == 'POST':
        form = NewRadiologyCommandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Radiology Command successfully sent!')
            return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')
    form = NewRadiologyCommandForm
    return render(request,
                  'main/make-radiology-command.html',
                  context={'form': form})


def print_appointments(request):
    return render(request=request,
                  template_name='main/final-appointments.html',
                  context={'finalschedules': FinalSchedule.objects.all})
