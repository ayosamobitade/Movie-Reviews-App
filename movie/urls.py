from django.urls import path
from .views import MovieHomeView, about


urlpatterns = [
    
    path('', MovieHomeView, name = 'homepage'),
    path('about/', about, name = 'aboutpage')

]