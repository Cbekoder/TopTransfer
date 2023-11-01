from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def clubs(request):
    return render(request, 'clubs.html')

def about(request):
    return render(request, 'about.html')