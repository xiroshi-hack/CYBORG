from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')


def browse(request):
    return render(request, 'includes/browse.html')