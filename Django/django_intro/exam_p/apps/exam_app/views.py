from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt
def login(request):
    return render(request, 'exam_app/login.html')


def regist(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
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
            user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = pw_hash)
            request.session['id'] = user.id
            return redirect('/login')
    else:
        return render(request, 'exam_app/regist.html')



def dashboard(request):
    context = {
        "user" : User.objects.get(id = request.session['id']),
        "trip" : Trip.objects.get(id = request.session['id']),
        "other_trips" : Trip.objects.exclude(id=request.session['id'])
    }
    return render(request, 'exam_app/dashboard.html', context)

def user_login(request):
    print("im at the user login in views")
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        print(errors, "*"*80)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        else: 
            user = User.objects.get(email = request.POST['email'])
            request.session['id'] = user.id
            return redirect('/dashboard')


def logout(request):
    request.session.clear()
    return redirect('/login')


def create(request):
    return render(request, 'exam_app/create.html')


def add_process(request):
    user = User.objects.get(id = request.session['id'])
    add_trip = Trip.objects.create(destination = request.POST['destination'], startdate = request.POST['startdate'], enddate = request.POST['enddate'], plan = request.POST['plan'])
    user.trips.add(add_trip)
    return redirect('/dashboard') 


def update(request, id):
    context = {
    "trip_info" : Trip.objects.get(id=id)
    }
    return render(request, 'exam_app/update.html', context)


def update_process(request, id):
    trip_update = Trip.objects.get(id = id)
    trip_update.destination = request.POST['destination']
    trip_update.startdate = request.POST['startdate']
    trip_update.enddate = request.POST['enddate']
    trip_update.plan = request.POST['plan']
    trip_update.save()
    return redirect('/dashboard')


def trip_info(request, id):
    context = {
    "trip" : Trip.objects.get(id = id),
    "user" : User.objects.get(id = request.session['id']),
    }
    return render(request, 'exam_app/trip_info.html', context)


def delete(request,id):
    trip = Trip.objects.get(id = id)
    trip.delete()
    return redirect('/dashboard')