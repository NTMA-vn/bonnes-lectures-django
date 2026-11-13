from django import forms
from .models import Book, Review, Author

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