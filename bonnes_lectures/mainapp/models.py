from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from .models import Book
class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    publisher = models.CharField(max_length=200)
    year = models.IntegerField()
    isbn = models.CharField(max_length=20)
    backCover = models.TextField()
    cover = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    publication_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
