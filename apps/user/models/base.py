# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator
from django.contrib.auth.hashers import make_password
from django.utils import timezone

# Project
from core.base_model import BaseModel

# Python
from datetime import datetime


class Position(BaseModel):

    POSITION = (
        ('HR', 'HR'),
        ('Project Manager', 'Project Manager'),
        ('Web Designer', 'Web Designer'),
        ('Frontend Engineer', 'Frontend Engineer'),
        ('Backend Engineer', 'Backend Engineer'),
        ('Mobile Engineer', 'Mobile Engineer'),
        ('Marketer', 'Marketer'),
        ('Manager', 'Manager')
    )
    position = models.CharField(max_length=70, choices=POSITION, unique=True)

    def __str__(self):
        return self.position


class User(AbstractUser):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    EMPLOYMENT_TYPE = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time')
    )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+998(12)345 67 89'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13)
    position = models.ManyToManyField(Position)
    birthday = models.DateField(blank=True, null=True)
    telegram = models.CharField(max_length=70, validators=[MinLengthValidator(4)], blank=True, null=True)
    image = models.ImageField(upload_to='profile_pic', default='employee.png')
    gender = models.CharField(max_length=6, choices=GENDER)
    employment_type = models.CharField(max_length=9, choices=EMPLOYMENT_TYPE)
    
    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.pk and self.password and not self.is_superuser:
            self.password = make_password(self.password)
        return super(User, self).save(*args, **kwargs)


class HardwareAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hardware')
    mac_address = models.CharField(max_length=19)

    def __str__(self):
        return f"{self.user.username} | {self.mac_address}"

    class Meta:
        verbose_name_plural = "Hardware Addresses"


class AssignedDevice(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    
    def __str__(self):
        return self.name


class OfficeHours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='office_hours')
    hours = models.PositiveSmallIntegerField(default=0)
    minutes = models.PositiveSmallIntegerField(default=0)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user} Hours: {str(self.hours)} Minutes: {str(self.minutes)} on date {str(self.date)}"


class WorkType(models.Model):
    ABSENT = 'Absent'
    AT_OFFICE = 'At office'
    REMOTE = 'Remote'
    WORK_TYPE = (
        (ABSENT, ABSENT),
        (AT_OFFICE, AT_OFFICE),
        (REMOTE, REMOTE)
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='work_type')
    work_type = models.CharField(max_length=30, choices=WORK_TYPE, null=True, blank=True)
    modified_datetime = models.DateTimeField()
    
    def __str__(self):
        return self.work_type
    
    def save(self, *args, **kwargs):
        self.modified_datetime = datetime.now()
        return super(WorkType, self).save(*args, **kwargs)