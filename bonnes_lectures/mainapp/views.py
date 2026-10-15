from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookForm, ReviewForm
from .models import Book, Review

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
    reviews = book.reviews.all()
    return render(request, 'mainapp/book.html', {'book': book, 'reviews': reviews})

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

def new_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('book', book_id=book.id)
    else:
        form = ReviewForm()
    return render(request, 'mainapp/new_review.html', {'form': form, 'book': book})

def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    book = review.book
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('book', book_id=book.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'mainapp/edit_review.html', {'form': form, 'review': review, 'book': book})

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    book = review.book
    if request.method == "POST":
        review.delete()
        return redirect('book', book_id=book.id)
    return render(request, 'mainapp/review_confirm_delete.html', {'review': review, 'book': book})