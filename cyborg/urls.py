from django.contrib.auth.views import LoginView
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup, name='signup'),
    path('browse/', browse, name="browse"),
    path('details/', details, name="details"),
    path('streams/', streams, name="streams"),
    path('profile/', profile, name="profile"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', LoginView.as_view(), name='login'),
    path('logoutconf/', logout_confirmation, name='logoutconf'),
]
