from django.db import models

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

# Create your models here.
