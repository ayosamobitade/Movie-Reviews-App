from django.shortcuts import render

# Create your views here.

def home(request):
    name = 'Ayobami'
    return render(request, "movie/home.html",
    {'name':name
    })

def MovieView(request):
    return render(request, 'movie/home.html')

def about(request):
    return render(request, 'movie/about.html')