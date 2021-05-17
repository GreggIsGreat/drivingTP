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
    path('all_students/', views.all_students, name='all_students')

]
urlpatterns += staticfiles_urlpatterns()
