from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class registerForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    omang_id = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    phonenumber = forms.CharField(max_length=30, required=False)
    city = forms.CharField(max_length=30, required=False)
    date_of_birth = forms.CharField(max_length=30, required=False)
    address = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'omang_id', 'city', 'date_of_birth', 'address',
            'phonenumber',
            'password1', 'password2',)


class addstudentForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    omang_id = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    phonenumber = forms.CharField(max_length=30, required=False)
    city = forms.CharField(max_length=30, required=False)
    date_of_birth = forms.CharField(max_length=30, required=False)
    address = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'omang_id', 'city', 'date_of_birth', 'address',
            'phonenumber',
            'password1', 'password2',)
