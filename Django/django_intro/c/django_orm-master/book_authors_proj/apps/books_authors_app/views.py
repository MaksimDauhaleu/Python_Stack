from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "library" : Book.objects.all(),
    }
    return render(request, 'books_authors_app/index.html', context)

def new(request):
    Book.objects.create(title=request.POST['name'], desc=request.POST['desc'])
    return redirect("/")

def authors(request):
    context = {
        "authors": Author.objects.all(),
    }
    return render(request, 'books_authors_app/authors.html',context)

def mew(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect("/authors")

def book_info(request, id):
    context={
        'spotlight' : Book.objects.get(id=id),
        "authors": Author.objects.all(),
    }
    return render(request, 'books_authors_app/view.html', context)

def add_author(request, id):
    new_auth = Author.objects.get(id=request.POST['author_add'])
    current_book = Book.objects.get(id=id)
    (current_book).authors.add(new_auth)
    current_book.save()
    return redirect(f'/book_info/{id}')

def author_info(request, id):
    context={
        'spotlight' : Author.objects.get(id=id),
        "books": Book.objects.all(),
        "published": Book.objects.filter(authors=id)
    }
    return render(request, 'books_authors_app/miew.html', context)

def add_book(request, id):
    new_book = Book.objects.get(id=request.POST['book_add'])
    current_author = Author.objects.get(id=id)
    (new_book).authors.add(current_author)
    new_book.save()
    return redirect(f'/author_info/{id}')