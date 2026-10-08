from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookForm
from .models import Book

def about(request):
    return HttpResponse(
        "Application Bonnes Lectures, développée en TP de Framework Web, Université d’Orléans, 2026."
    )

def welcome(request):
    return render(request, 'mainapp/welcome.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'mainapp/book_list.html', {'books': books})

def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'mainapp/book.html', {'book': book})

def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book', book_id=book.id)
    else:
        form = BookForm()
    return render(request, 'mainapp/book_form.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'mainapp/book_form.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'mainapp/book_confirm_delete.html', {'book': book})

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'mainapp/book_form.html', {'form': form, 'book': book})