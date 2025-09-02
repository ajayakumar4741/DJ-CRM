from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import RegForm
from . models import *
# Create your views here.


def index(request):
    records = Records.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(username=username, password=password)
        # Check if user logged in
        if user:
            login(request, user)
            messages.success(request,'Successfully logged in!')
            return redirect('index')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('index')
    return render(request,'index.html',{'records':records})

def record(request,pk):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,'You Have Been Logged Out...')
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have Successfully Registered...')
            return redirect('index')
    else:
        form = RegForm()
    return render(request,'reg.html',{'form':form})
    # return render(request,'reg.html',{'form':form})