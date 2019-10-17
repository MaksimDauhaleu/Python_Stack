from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def login(request):
    return render(request, 'login_app/login.html')

def regist(request):
    if request.method == "POST":
        print("POST in views:", request.POST)
        errors = Regist.objects.reg_validator(request.POST)
        print(errors)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/regist')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            print(password)
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            print(pw_hash)
            user = Regist.objects.create(first_name = first_name, last_name = last_name, email = email, password = pw_hash)
            request.session['id'] = user.id
            return redirect('/login')
    else:
        return render(request, 'login_app/regist.html')



def success(request):
    context = {
        "user" : Regist.objects.get(id = request.session['id']),
    }
    return render(request, 'login_app/success.html', context)

def user_login(request):
    print("im at the user login in views")
    if request.method == "POST":
        errors = Regist.objects.login_validator(request.POST)
        print(errors, "*"*80)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        else: 
            user = Regist.objects.get(email = request.POST['email'])
            request.session['id'] = user.id
            return redirect('/success')
def logout(request):
        request.session.clear()
        return redirect('/login')

#################################################################################################
                    

def post_massage(request):
    user = Regist.objects.get(id = id)
    Messages.ob