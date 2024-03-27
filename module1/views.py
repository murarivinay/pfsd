import string

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

from requests import auth

from .models import *



# Create your views here.
def hello1(request):
    return HttpResponse("<center>welcome to TTM HomePage</center>")

def NewHomePage(request):
    return render(request,'newhomepage.html')

def travelpackage(request):
    return render(request,'travelpackage.html')

def print1(request):
    return render(request,'print_to_console.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input:{user_input}')
    a1={'user_input': user_input}
    return render(request,'print_to_console.html',a1)



def randomcall(request):
    return render(request,'randomotpgenerater.html')

def randomlogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input:{user_input}')
        a2=int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))
    a1={'ran1': ran1}
    return render(request,'randomotpgenerater.html',a1)

def getdate1(request):
    return render(request, 'datetime.html')


import datetime
from django.shortcuts import render
def get_date(request):
    if request.method=='POST':
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+datetime.timedelta(days=integer_value)
            return render(request,'datetime.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'datetime.html',{'form':form})

def register1(request):
    return render(request,'registerloginform.html')


def registerloginfunction(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')

        if Register.objects.filter(email=email).exists():
            return HttpResponse("Email already registered .choose a different email .")
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('NewHomePage')
    return render(request,'registerloginform.html')

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})

def rent(request):
    return render(request,'rent.html')



import requests
def weatherpagecall(request):
    return render(request,'weatherappinput.html')
def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'c788ed6e3b7395b729e973c6178ed595'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})



def feedback(request):
    return render(request,'feedbackform.html')


def feedbackfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback')
        phonenumber = request.POST.get('phonenumber')
        tosend = feedback_text + 'ThankYou'

        Feedback.objects.create(name=name, email=email, feedback=feedback_text, phonenumber=phonenumber)
        send_mail(
            'Thank You for Contacting shashank Travel Tourism and Manage',
            tosend,
            '2200032512cseh@gmail.com',
            [email],
            fail_silently=False,

        )
        return redirect('NewHomePage')

    return render(request, 'feedbackform.html')



def signup(request):
    return render(request,'signup.html')

from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render

def signup1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password1')

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists.')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account Created Successfully!')
                return render(request, 'newhomepage.html')
        else:
            messages.info(request, 'Passwords do not match')
            return render(request, 'signup.html')
    else:
        # Handle GET request (display the signup form)
        return render(request, 'signup.html')

def login(request):
    return render(request,'login.html')

from django.shortcuts import redirect

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(request, username=username, password=pass1)

        if user is not None:
            auth.login(request, user)
            return redirect('NewHomePage')  # Replace with the actual view name or URL pattern
        else:
            messages.info(request, 'Invalid Credentials.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')

