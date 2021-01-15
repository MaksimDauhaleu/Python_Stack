from django.shortcuts import render, redirect
from .models import *


def page(request):
    # context={
    #     "library" : Book.objects.all(),
    # }
    return render(request, 'marketFirst/index.html')

def login(request):
    return render(request, 'marketFirst/login.html')