from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')


def browse(request):
    return render(request, 'includes/browse.html')


def details(request):
    return render(request, 'includes/details.html')
    


def streams(request):
    return render(request, 'includes/streams.html')