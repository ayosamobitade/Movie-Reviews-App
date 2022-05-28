from django.shortcuts import render
from .models import Movie

# Create your views here.

def MovieHomeView(request):
    name = 'Ayobami'
    searchTerm = request.GET.get('searchMovie')
    movies = Movie.objects.all()
    return render(request, "movie/home.html",
    {'name':name,
    'searchTerm':searchTerm,
    'movies':movies
    })



def about(request):
    return render(request, 'movie/about.html')


def SignupView(request):
    email = request.GET.get('email')
    return render(request, 'movie/signup.html',
    {
        'email':email
    })