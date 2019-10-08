from django.shortcuts import render, redirect

def gold(request):
    return render(request, 'gold_app/gold.html')


def 