from django.urls import path
from .views import MovieHomeView, about, SignupView


urlpatterns = [
    
    path('', MovieHomeView, name = 'homepage'),
    path('about/', about, name = 'aboutpage'),
    path('signup', SignupView, name = 'signuppage')

]