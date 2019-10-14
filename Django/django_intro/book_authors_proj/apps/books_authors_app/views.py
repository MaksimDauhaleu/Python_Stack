from django.shortcuts import render, redirect
from .models import *


def page(request):
    context={
        "library" : Book.objects.all(),
    }
    return render(request, 'books_authors_app/index.html', context)


def book_info(request, id):
    context={
        "spotlight" : Book.objects.get(id=id),
        "authors": Author.objects.all(),
    }
    return render(request, 'books_authors_app/books.html', context)

def add_author(request, id):
    new_auth = Author.objects.get(id=request.POST['author_add'])
    current_book = Book.objects.get(id=id)
    (current_book).authors.add(new_auth)
    current_book.save()
    return redirect(f'/book_info/{id}')

def add_book(request, id):
    new_book = Book.objects.get(id=request.POST['book_add'])
    current_author = Author.objects.get(id=id)
    (new_book).authors.add(current_author)
    new_book.save()
    return redirect(f'/author_info/{id}')