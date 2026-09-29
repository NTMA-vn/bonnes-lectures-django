from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

def about(request):
    return HttpResponse("Application Bonnes Lectures, développée en TP de Framework Web, Université d’Orléans, 2026.")

def welcome(request):
    return render(request, 'mainapp/welcome.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'mainapp/book_list.html', {'books': books})