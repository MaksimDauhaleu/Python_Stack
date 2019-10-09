from django.shortcuts import render, redirect


def gold(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    return render(request, 'gold_app/gold.html')

# def process_farm(request):

