from django.shortcuts import render, redirect
from .forms import *
from .models import *

def home(request):
    
    header = Header.objects.all()
    most = MostPop.objects.all()
    library = Library.objects.all()
    
    return render(request, 'pages/home.html', {
        "info":header,
        "most":most,
        "library":library,
        })


def browse(request):
    
    games = Games.objects.all() 
    top = Top.objects.all() 
    live = LiveStream.objects.all() 
    popular = Popular.objects.all()
    
    return render(request, 'includes/browse.html', {
        "games": games,
        "top": top,
        "live": live,
        "popular": popular,
    })


def details(request):
    return render(request, 'includes/details.html')
    


def streams(request):
    return render(request, 'includes/streams.html')



def profile(request):
    return render(request, 'includes/profile.html')


def signup(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'registration/signup.html', {"form": form})



def logout(request):
    return render(request, 'registration/logout.html')


def logout_confirmation(request):
    return render(request, 'registration/logout-confirmation.html')