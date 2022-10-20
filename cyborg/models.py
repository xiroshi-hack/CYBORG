from email.policy import default
from turtle import title
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    
    
class Header(models.Model): 
    title = models.CharField(max_length=150, default='Welcome To Cyborg')
    text = models.CharField(max_length=200, default='BROWSE OUR POPULAR GAMES HERE')
    btn = models.CharField(max_length=50, default='Browse Now')
    
    def __str__(self):
        return self.title
    
    
class MostPop(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=100, default='game')
    text = models.CharField(max_length=100)