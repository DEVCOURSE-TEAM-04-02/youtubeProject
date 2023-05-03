from .models import *
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/data.html') 

def detail(request):
    return render(request, 'main/detail.html') 