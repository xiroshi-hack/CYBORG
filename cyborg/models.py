from email.policy import default
from statistics import mode
from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    
    
class Header(models.Model): 
    title = models.CharField(max_length=150, default='Welcome To Cyborg')
    text = models.CharField(max_length=200, default='BROWSE OUR POPULAR GAMES HERE')
    btn = models.CharField(max_length=50, default='Browse Now')
    