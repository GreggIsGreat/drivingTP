from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Student


class registerForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    omang_id = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    phonenumber = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    date_of_birth = forms.CharField(max_length=30)
    address = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'omang_id',
            'city',
            'date_of_birth',
            'address',
            'phonenumber',
            'password1',
            'password2',)


class Studentform(ModelForm):
    class Meta:
        model = Student
        fields = ('name',
                  'omang_id',
                  'email',
                  'gender',
                  'phonenumber',
                  'DateOfBirth',
                  'course1',
                  'course2',
                  'Purpose')


class ResultForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name',
                  'result1',
                  'result2',
                  'DateOfBirth',
                  'gender')


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name',
                  'email',
                  'Purpose',)


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        profile = kwargs.get('instance')

        if profile:
            kwargs['instance'] = profile.user
        self.user_form = EditUserForm(*args, **kwargs)
        self.fields.update(self.user_form.fields)
        self.initial.update(self.user_form.initial)

    def save(self, *args, **kwargs):
        self.user_form.save(*args, **kwargs)
        return super(EditProfileForm, self).save(*args, **kwargs)

    class Meta:
        model = User
        exclude = ('user',)
