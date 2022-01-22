from django.shortcuts import render

# Create your views here.
from .models import city
from .forms import CityForm


def index(request):
    return render(request , 'index.html' ,  {})