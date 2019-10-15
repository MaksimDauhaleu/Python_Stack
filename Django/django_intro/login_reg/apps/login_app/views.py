from django.shortcuts import render, redirect


def login(request):
    return render(request, 'login_app/login.html')

def regist(request):
    return render(request, 'login_app/regist.html')