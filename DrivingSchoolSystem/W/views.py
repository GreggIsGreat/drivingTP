from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import registerForm
from .models import Student
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, 'W/home.html')


def navbar(request):
    return render(request, 'W/navbar.html')


def Register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = registerForm()
    return render(request, 'W/register.html', {'form': form})


def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'W/login.html', context={'form': form})


def Logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


def addstudent(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = registerForm()
    return render(request, 'W/addstudent.html')


def payment(request):
    return render(request, 'W/payment.html')


def all_students(request):
    student = Student.objects.all()
    return render(request, 'W/Student.html', context={'student': student})


def addstudent(request):
    return render(request, 'W/home.html')
