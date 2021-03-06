from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def login(request):
    return render(request, 'exam_app/login.html')

def regist(request):
    if request.method == "POST":
        errors = Regist.objects.reg_validator(request.POST)
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
        return render(request, 'exam_app/regist.html')



def success(request):
    context = {
        "user" : Regist.objects.get(id = request.session['id']),
        "trips" : Trip.objects.all(),
    }
    return render(request, 'exam_app/success.html', context)

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
##########

def add_trip(request):
    new_trip = Trip.objects.create(destination = request.POST['destination'], startdate = request.POST['startdate'], enddate = request.POST['enddate'], plan = request.POST['plan'])
    user = Regist.objects.get(id=request.session.id)
    user.trips.add(new_trip)
    user.save()
    return redirect('/success')

def create(request,id):
    context = {
        "read" : Trip.objects.get(id=id),
    }
    return render(request, 'exam_app/create.html',context)

def read(request, id):
    context = {
        "read" : Trip.objects.get(id=id),
    }
    return render(request,'exam_app/read.html',context)

def edit(request, id):
    context = {
        "trip" : Trip.objects.get(id=id),
    }
    return render(request,'exam_app/edit.html',context)


def update(request, id):
    if request.method == "POST":
        trip = Trip.objects.get(id = id)
        errors = Trip.objects.trip_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/read/{trip.id}/update')
        else:
            destination = request.POST['destination']
            startdate = request.POST['startdate']
            enddate = request.POST['enddate']
            plan = request.POST['plan']
            user = Trip.objects.create(destination = destination, startdate = startdate, enddate = enddate, plan = plan)
            print("*"*80)
            user.save()
            return redirect('/success')
    else:
        return render(request, 'exam_app/create.html')


def delete(request,id):
    delete = Trip.objects.get(id=id)
    delete.delete()
    return redirect('/success')