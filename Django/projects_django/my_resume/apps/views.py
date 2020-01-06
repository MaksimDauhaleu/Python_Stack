from django.shortcuts import render


def index(req):
    return render(req,'index.html')

def contact(req):
    return render(req,"contact.html")

def resume(req):
    return render(req,"resume.html")

def portfolio(req):
    return render(req,"portfolio.html")

def about(req):
    return render(req,"about.html")