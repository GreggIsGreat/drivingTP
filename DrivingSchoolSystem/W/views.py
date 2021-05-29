from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.shortcuts import render
from .decorators import allowed_users
from .forms import registerForm, Studentform, ResultForm, UpdateProfileForm
from .models import Student


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
            group = Group.objects.get(name='Student')
            user.groups.add(group)
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
    myresults = Student.objects.filter(name=request.user)
    return render(request, 'W/results.html', {'myresults': myresults})


@login_required()
@allowed_users(allowed_roles=['Admin', 'StaffDashboard'])
def StaffDashboard(request):
    Maindata = Student.objects.all()
    return render(request, 'W/StaffDashboard.html', {'Maindata': Maindata})


@login_required()
def Profile(request):
    UserProfile = Student.objects.filter(name=request.user)
    return render(request, 'W/Profile.html', {'UserProfile': UserProfile})


@login_required()
def registercourses(request):
    submitted = False
    if request.method == "POST":
        form = Studentform(request.POST)
        if form.is_valid():

            form.save()
            return redirect('/registercourses? submitted=True')
        else:
            form = Studentform
            if 'sumbitted' in request.GET:
                submitted = True
    form = Studentform
    return render(request, 'W/registercourses.html', {'form': form, 'submitted': submitted})


def allstudents(request):
    allstudents = Student.objects.all()
    return render(request, 'W/allstudents.html', {'allstudents': allstudents})


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
def editProfile(request):
    form = UpdateProfileForm(data=request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('Profile')

    context = {'form': form}
    return render(request, 'W/editProfile.html', context)


@login_required
def updatestudentresults(request):
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('StaffDashboard')
    else:
        form = ResultForm(instance=request.user)
        args = {'form': form}
        return render(request, 'W/updatestudentresults.html', args)


def changepasswords(request):
    return render(request, 'W/changepasswords.html', {'changepasswords': changepasswords})