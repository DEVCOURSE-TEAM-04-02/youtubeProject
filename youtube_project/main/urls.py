from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.main, name='data'),
    path('detail', views.detail, name='detail'),
    #path('<str:channel_id>/', views.detail, name='detail'), #아직 DB가 만들어지지 않아서
]
