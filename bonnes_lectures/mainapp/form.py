from django import forms
from .models import Book

class BookForm(forms.ModelForm):
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