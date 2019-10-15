from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = { 
        "library" : Show.objects.all(),
    }
    return render(request, 'tv_show/index.html', context)

def create(request):
    return render(request, 'tv_show/create.html')


def show(request, id):
    context = {
        "show" : Show.objects.get(id=id),
    }
    return render(request, 'tv_show/show.html', context)

def add_show(request):
    new_show = Show.objects.create(title = request.POST['title'], network = request.POST['network'], desc = request.POST['desc'])
    return redirect(f'/show/{new_show.id}')

def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/show/{id}/edit')

    else:
        show = Blog.objects.get(id = id)
        show.name = request.POST['name']
        show.desc = request.POST['desc']
        show.desc = request.POST['desc']
        show.save()
        messages.success(request, "Blog successfully updated")
        return redirect(f'/show/')


def read(request, id):
    context = {
        "read" : Show.objects.get(id=id),
    }
    return render(request,'tv_show/read_one.html',context)


def delete(request, id):
    delete = Show.objects.get(id=id)
    delete.delete()
    return redirect('/')

def edit(request, id):
    context = {
        "show" : Show.objects.get(id=id),
    }
    #new_show = Show.objects.create(title = request.POST['title'], network = request.POST['network'], desc = request.POST['desc'])
    return render(request,'tv_show/edit.html',context)
