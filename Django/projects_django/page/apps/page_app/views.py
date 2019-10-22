from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *


# Create your views here.
def index(request):
    sneakers = Sneaker.objects.all()
    sneakers = sneakers[:3]
    context = {'sneakers': sneakers}
    return render(request, 'page_app/index.html', context)


def detail(request, sneaker_id):
    sneaker = get_object_or_404(Sneaker, pk=sneaker_id)
    context = {'sneaker': sneaker}
    return render(request, 'page_app/detail.html', context)


def about(request):
    return render(request, 'page_app/about.html')


def catalog(request):
    sneakers = Sneaker.objects.all()
    context = {'sneakers': sneakers}
    return render(request, 'page_app/catalog.html', context)