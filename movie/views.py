from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "movie/home.html")

def MovieView(request):
    return render(request, 'home.html')