from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'tv_show/index.html')
