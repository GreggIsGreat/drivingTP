from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('navbar/', views.navbar, name='navbar'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('register/', views.Register, name='Register'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('payment/', views.payment, name='payment'),
    path('Dashboard/', views.Dashboard, name='Dashboard'),
    path('Student_Dashboard/', views.Student_Dashboard, name='Student_Dashboard'),
    path('results/', views.results, name='results'),
    path('StaffDashboard/', views.StaffDashboard, name='StaffDashboard'),
    path('Profile/', views.Profile, name='Profile'),
    path('updatestudentresults/', views.updatestudentresults, name='updatestudentresults'),
    path('editProfile/', views.editProfile, name='editProfile'),

]
urlpatterns += staticfiles_urlpatterns()
