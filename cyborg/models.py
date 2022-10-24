from email.policy import default
from random import choices
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


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
    

    
class Library(models.Model):
    DOWNLOAD = "download"
    LOADED = "loaded"    
    
    LIBRARY_CHOICES = [
        (DOWNLOAD, "download"),
        (LOADED, "loaded")
    ]
    
    img = models.ImageField()
    game = models.CharField(max_length=50, default='dota')
    date = models.TimeField(default=timezone.now())
    type = models.CharField(max_length=10, choices=LIBRARY_CHOICES)
    
    def __str__(self):
        return self.game
    
    
    