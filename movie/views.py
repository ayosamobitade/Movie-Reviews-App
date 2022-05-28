from django.shortcuts import render

# Create your views here.

def MovieHomeView(request):
    name = 'Ayobami'
    return render(request, "movie/home.html",
    {'name':name
    })



def about(request):
    return render(request, 'movie/about.html')