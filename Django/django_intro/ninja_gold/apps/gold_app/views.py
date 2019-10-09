from django.shortcuts import render, redirect
import random

def gold(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    return render(request, 'gold_app/gold.html')


def process(request):
    print("*"*50)
    if request.method == "POST":
        if 'farm' in request.POST:
            request.session['gold'] += random.randint(10,20)
        if 'cave' in request.POST:
            request.session['gold'] += random.randint(5,10)
        if 'house' in request.POST:
            request.session['gold'] += random.randint(2,5)
        if 'casino' in request.POST:
            request.session['gold'] += random.randint(-50,50)
    return redirect('/')