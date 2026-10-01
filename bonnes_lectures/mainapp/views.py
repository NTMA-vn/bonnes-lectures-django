from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Book

def about(request):
    return HttpResponse("Application Bonnes Lectures, développée en TP de Framework Web, Université d’Orléans, 2026.")

def welcome(request):
    return render(request, 'mainapp/welcome.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'mainapp/book_list.html', {'books': books})

def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'mainapp/book.html', {'book': book})