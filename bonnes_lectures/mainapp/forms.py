from django import forms
from .models import Book, Review, Author
from .isbn import IsbnField


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name"]
        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
        }
        help_texts = {
            "first_name": "Facultatif pour les auteurs à nom unique ou pseudonymes.",
        }


class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.order_by('last_name', 'first_name'),
        label="Auteur(s)",
    )
    isbn = IsbnField(
        label="ISBN",
        help_text="Saisissez un ISBN-10 ou ISBN-13 valide (ex. 978-2070360536).",
    )

    class Meta:
        model = Book
        fields = ["authors", "title", "publisher", "year", "isbn", "backCover", "cover"]
        labels = {
            "authors": "Auteur(s)",
            "title": "Titre",
            "publisher": "Maison d'édition",
            "year": "Année",
            "isbn": "ISBN",
            "backCover": "Présentation",
            "cover": "Couverture disponible",
        }
        help_texts = {
            "authors": "Maintenez Ctrl (ou Cmd sur Mac) pour sélectionner plusieurs auteurs.",
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["body", "rating"]
        labels = {
            "body": "Avis",
            "rating": "Note (sur 5)",
        }