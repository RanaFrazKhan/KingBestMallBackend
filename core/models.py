from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class States(models.Model):
    Name = models.CharField(max_length=255)

class Cities(models.Model):
    state=models.ForeignKey(States,on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)

class Contact_Us(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    Message = models.CharField(max_length=10000000, blank=False)

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('A', 'Admin'),
        ('S', 'Super'),
        ('U', 'User'),
        ('V', 'Vendor'),
    )
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default='U')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='0')
    Fname = models.CharField(max_length=255)
    Lname = models.CharField(max_length=255)
    Mobile = models.CharField(max_length=255,blank=True)
    Country = models.CharField(max_length=255,blank=True)
    State = models.CharField(max_length=255,blank=True)
    City = models.CharField(max_length=255,blank=True)
    Zip = models.CharField(max_length=255,blank=True)
    Address = models.CharField(max_length=10000000, blank=True)
    Pic = models.TextField(blank=True)
    Complete = models.BooleanField(default=False)
    ISConfirmed = models.BooleanField(default=False)
    Activation_Key = models.CharField(max_length=255, blank=True, default='')
    def __str__(self):
        return str(self.user)

class Subscription(models.Model):
    Email = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return str(self.Email)