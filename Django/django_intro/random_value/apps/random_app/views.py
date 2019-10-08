from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def random_number(request):
        if 'count' not in request.session:
            request.session['count'] = 1
        else :
            request.session['count']+=1
        context = {
            "random" : get_random_string(length=34),
            "count" : request.session['count'],
        }

        if request.method == "POST":
            print(request.POST["text1"])
        return render(request, "random_app/random.html", context)

def my_name(request):
        
    context = {
        "name" : request.POST["text1"]
    }
    return render(request, "random_app/name.html", context)


def reset(request):
    request.session.clear()
    return redirect("/")

