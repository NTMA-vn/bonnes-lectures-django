from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import PermissionDenied
from django.db.models import ProtectedError
from .forms import BookForm, ReviewForm, AuthorForm
from .models import Book, Review, Author
def author_list(request):
    authors = Author.objects.order_by('last_name', 'first_name')
    return render(request, 'mainapp/author_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = author.books.all()
    return render(request, 'mainapp/author_detail.html', {'author': author, 'books': books})

def new_author(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('author_detail', author_id=author.id)
    else:
        form = AuthorForm()
    return render(request, 'mainapp/author_form.html', {'form': form})

def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if not request.user.is_authenticated or (author.user != request.user and not request.user.is_superuser):
        raise PermissionDenied
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_detail', author_id=author.id)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'mainapp/author_form.html', {'form': form, 'author': author})

def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if not request.user.is_authenticated or (author.user != request.user and not request.user.is_superuser):
        raise PermissionDenied
    error_message = None

    if request.method == "POST":
        try:
            author.delete()
            return redirect('author_list')
        except ProtectedError:
            error_message = (
                f"Impossible de supprimer cet auteur : {author.books.count()} livre(s) "
                f"lui sont encore associé(s). Supprimez d'abord ses livres !"
            )

    return render(request, 'mainapp/author_confirm_delete.html', {
        'author': author,
        'error_message': error_message,
    })
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
    if not request.user.is_authenticated:
            return redirect('login')
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book', book_id=book.id)
    else:
        form = BookForm()
    return render(request, 'mainapp/book_form.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if not request.user.is_authenticated or (book.user != request.user and not request.user.is_superuser):
        raise PermissionDenied
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
    if not request.user.is_authenticated or (book.user != request.user and not request.user.is_superuser):
        raise PermissionDenied
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'mainapp/book_confirm_delete.html', {'book': book})

def new_review(request, book_id):
    if not request.user.is_authenticated:
            return redirect('login')
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book', book_id=book.id)
    else:
        form = ReviewForm()
    return render(request, 'mainapp/new_review.html', {'form': form, 'book': book})

def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if not request.user.is_authenticated or (review.user != request.user and not request.user.is_superuser):
        raise PermissionDenied
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
    if not request.user.is_authenticated or (review.user != request.user and not request.user.is_superuser):
        raise PermissionDenied
    book = review.book
    if request.method == "POST":
        review.delete()
        return redirect('book', book_id=book.id)
    return render(request, 'mainapp/review_confirm_delete.html', {'review': review, 'book': book})