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
    
    def __str__(self):
        return self.title
    

    
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
    
    
    
class Games(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=40, default='game name')
    
    def __str__(self):
        return self.name
    


class Top(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=40, default='game name')
    type = models.CharField(max_length=50, default="sandbox")
    
    def __str__(self):
        return self.name
    

class LiveStream(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title