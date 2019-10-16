from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def login(request):
    return render(request, 'login_app/login.html')

def regist(request):
    if request.method == "POST":
        errors = Regist.objects.basic_validator(request.POST)
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
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())   
            print(pw_hash)
            user = Regist.objects.create(first_name = first_name, last_name = last_name, email = email, password = pw_hash)
            return redirect('/login')
    else:
        return render(request, 'login_app/regist.html')

def add_user(request):
    new_user = Regist.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'], conf_password = request.POST['conf_password'])
    return redirect('/login')

def success(request):

    return render(request, 'login_app/success.html')

def user_login(request):
    errors={}
    print("login user works!"+"*"*80)
    if request.method == "POST":
        other_user = Regist.objects.filter(email = request.POST['email'])
        #print(other_user)
        #print(request.POST)
        try:
            this_user = other_user[0]
            if request.POST['password'] == this_user.password:
                
                return redirect("/success")
            errors["password_error"] = "You forgot your password"
        except:
            errors['email_error']= "No user exists here, go ahead and register"
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
    return redirect("/success")
