from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Admin(models.Model):
    name = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20, blank=True, primary_key=True)
    omang_id = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    male = 'male'
    female = 'female'

    gender_CHOICES = [
        (male, 'male'),
        (female, 'female'),
    ]
    gender = models.CharField(
        max_length=7,
        choices=gender_CHOICES,
        default=None,
    )
    phonenumber = models.CharField(max_length=20, blank=True)
    course1 = models.CharField(max_length=20, blank=True)
    course2 = models.CharField(max_length=20, blank=True)
    result1 = models.CharField(max_length=20, blank=True)
    result2 = models.CharField(max_length=20, blank=True)
    DateOfBirth = models.DateField(max_length=20, blank=True)
    New = 'NW'
    Renewal = 'RL'

    Purpose_CHOICES = [
        (New, 'New'),
        (Renewal, 'Renewal'),
    ]
    Purpose = models.CharField(
        max_length=2,
        choices=Purpose_CHOICES,
        default=New,
    )
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=20, blank=True)
    omang_id = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.name
