from django.urls import path
from .views import MovieView


urlpatterns = [
    path('movie', MovieView, name = "home"),

]