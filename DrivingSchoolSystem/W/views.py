from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from .decorators import allowed_users
from .forms import registerForm, Studentform, ResultForm, UpdateProfileForm
from .models import Student, Staff


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


@login_required()
def addstudent(request):
    return render(request, 'W/addstudent.html')


@login_required()
def payment(request):
    return render(request, 'W/payment.html')


@login_required()
@allowed_users(allowed_roles=['Student', 'Admin'])
def Student_Dashboard(request):
    return render(request, 'W/Student.html')


@login_required()
@allowed_users(allowed_roles=['Admin'])
def addstudentform(request):
    return render(request, 'W/home.html')


@login_required()
@allowed_users(allowed_roles=['Admin'])
def Dashboard(request):
    return render(request, 'W/dashboard.html')


@login_required()
@allowed_users(allowed_roles=['Student', 'Admin'])
def results(request):
    myresults = Student.objects.all()
    return render(request, 'W/results.html', {'myresults': myresults})


@login_required()
@allowed_users(allowed_roles=['Admin', 'StaffDashboard'])
def StaffDashboard(request):
    Maindata = Student.objects.all()
    return render(request, 'W/StaffDashboard.html', {'Maindata': Maindata})


@login_required
def updatestudentresults(request):
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ResultForm(instance=request.user)
        args = {'form': form}
        return render(request, 'W/updatestudentresults.html', args)


@login_required()
def Profile(request):
    UserProfile = Student.objects.all()
    return render(request, 'W/Profile.html', {'UserProfile': UserProfile})


@login_required()
def addstudent(request):
    submitted = False
    if request.method == "POST":
        form = Studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/addstudent? submitted=True')
        else:
            form = Studentform
            if 'sumbitted' in request.GET:
                submitted = True
    form = Studentform
    return render(request, 'W/addstudent.html', {'form': form, 'submitted': submitted})


@login_required()
@allowed_users(allowed_roles=['Student', 'Admin'])
def Student_Dashboard(request):
    student = Student.objects.all()
    return render(request, 'W/Student.html', context={'student': student})


@login_required()
@allowed_users(allowed_roles=['Student', 'Admin'])
def editProfile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('Profile'))
    else:
        form = UpdateProfileForm(instance=request.user)
        args = {'form': form}
    return render(request, 'W/editProfile.html', args)
