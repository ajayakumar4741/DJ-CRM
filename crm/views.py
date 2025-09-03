from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import RegForm, AddRecordForm
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
    if request.user.is_authenticated:
        customer_record = Records.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.error(request,'You Must Be Logged in to access that page...')
        return redirect('index')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_item = Records.objects.get(id=pk)
        delete_item.delete()
        messages.success(request,'Record Deleted Successfully...')
        return redirect('index')
    else:
        messages.error(request,'You Must Be Logged in to delete records...')
        return redirect('index')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record Added...')
                return redirect('index')
        else:
            return render(request,'add.html',{'form':form})
    else:
        messages.error(request,'You Must Be Logged in to add records...')
        return redirect('index')

def update_record(request,pk):
    if request.user.is_authenticated:
        current_user = Records.objects.get(id=pk) 
        form = AddRecordForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated...')
            return redirect('index')
        else:
            return render(request,'update.html',{'form':form})
    else:
        messages.error(request,'You Must Be Logged in to update records...')
        return redirect('index')

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