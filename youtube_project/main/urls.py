from django.urls import path
from . import views
from .views import *

app_name= 'main'
urlpatterns = [
    path('', views.animal, name='data'),
    path('<str:channel_id>/', views.detail, name='detail'),
    path("animal.html", views.animal, name='animal'),
    path("movie.html", views.movie, name='movie'),
    path("game.html", views.game, name='game'),
    path("sport.html", views.sport, name='sport'),
    path("food.html", views.food, name='food'),
   #path('<str:channel_id>/', views.detail, name='detail'), #아직 DB가 만들어지지 않아서
]
