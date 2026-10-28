from django import forms
from .models import Book, Review, Author

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.order_by('last_name', 'first_name'),
        label="Auteur",
        empty_label=" Choisissez un auteur",)
    class Meta:
        model = Book
        fields = ["author","title","publisher","year","isbn","backCover","cover",]
        labels = {
            "author": "Auteur",
            "title": "Titre",
            "publisher": "Maison d'édition",
            "year": "Année",
            "isbn": "ISBN",
            "backCover": "Présentation",
            "cover": "Couverture disponible",
        }
        help_texts = {"author": "Sélectionnez l'auteur de l'ouvrage dans la liste.",}
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["body", "rating"]
        labels = {
            "body": "Avis",
            "rating": "Note (sur 5)",
        }