from django.urls import path
from .views import MovieView, home, about


urlpatterns = [
    path('movie', MovieView, name = "home"),
    path('', home, name = 'homepage'),
    path('about/', about, name = 'aboutpage')

]