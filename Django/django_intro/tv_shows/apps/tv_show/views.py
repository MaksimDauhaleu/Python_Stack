from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = { 
        "library" : Show.objects.all(),
    }
    return render(request, 'tv_show/index.html', context)

def add_show(request):
    return render(request, 'tv_show/create.html')

def create_b(request):
    return redirect(request, 'tv_show/create.html')