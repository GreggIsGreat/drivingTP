from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.Admin = None

    def __str__(self):
        return self.Admin


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.Staff = None

    def __str__(self):
        return self.Staff


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.course_name


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True)
    omang_id = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=20, blank=True)
    course1 = models.CharField(max_length=20, blank=True)
    course2 = models.CharField(max_length=20, blank=True)
    course3 = models.CharField(max_length=20, blank=True)
    result1 = models.CharField(max_length=20, blank=True)
    result2 = models.CharField(max_length=20, blank=True)
    result3 = models.CharField(max_length=20, blank=True)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.Student = None

    def __str__(self):
        return self.Student


class LeaveReportStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class StudentResult(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_Practical_marks = models.FloatField(default=0)
    eye_marks = models.FloatField(default=0)
    course_final_marks = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
