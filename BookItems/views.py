from django.shortcuts import render
from .models import Book

def homePage(req):
    books = Book.objects.all()
    return render(req, 'BookItems/_index.html', {'books': books})
