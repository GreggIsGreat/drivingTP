# Generated by Django 3.2 on 2021-05-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('omang_id', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False)),
                ('omang_id', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default=None, max_length=7)),
                ('phonenumber', models.CharField(blank=True, max_length=20)),
                ('course1', models.CharField(blank=True, max_length=20)),
                ('course2', models.CharField(blank=True, max_length=20)),
                ('result1', models.CharField(blank=True, max_length=20)),
                ('result2', models.CharField(blank=True, max_length=20)),
                ('DateOfBirth', models.DateField(max_length=20, null=True)),
                ('Purpose', models.CharField(choices=[('NW', 'New'), ('RL', 'Renewal')], default='NW', max_length=2)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
