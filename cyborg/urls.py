from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('browse/', browse, name="browse"),
    path('details/', details, name="details"),
    path('streams/', streams, name="streams"),
    path('profile/', profile, name="profile"),
    path("accounts/", include("django.contrib.auth.urls")),
]
