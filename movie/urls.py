from django.urls import path
from .views import MovieView, home


urlpatterns = [
    path('movie', MovieView, name = "home"),
    path('', home, name = 'homepage')

]