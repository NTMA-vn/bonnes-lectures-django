from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .isbn import Isbn
from .forms import BookForm
from .models import Author, Book


class IsbnTests(TestCase):
    def test_valid_isbn13(self):
        isbn = Isbn("978-2070360536")
        self.assertEqual(isbn.prefix, "978")
        self.assertEqual(isbn.check_digit, "6")
        self.assertEqual(int(isbn), 9782070360536)
        self.assertEqual(str(isbn), "978-2-0703-6053-6")

    def test_invalid_isbn13_checksum(self):
        with self.assertRaises(ValidationError):
            Isbn("978-2070360530")

    def test_valid_isbn10_with_x(self):
        isbn = Isbn("0-8044-2957-X")
        self.assertIsNone(isbn.prefix)
        self.assertEqual(isbn.check_digit, "X")
        self.assertEqual(str(isbn), "0-8044-2957-X")

    def test_invalid_isbn_length(self):
        with self.assertRaises(ValidationError):
            Isbn("12345")


class BookFormTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Isaac", last_name="Newton")

    def test_book_form_valid_isbn(self):
        form = BookForm(data={
            "authors": [self.author.id],
            "title": "Pommme",
            "publisher": "TRAN",
            "year": 1951,
            "isbn": "978-2070360536",
            "backCover": "hello.",
            "cover": False,
        })
        self.assertTrue(form.is_valid())

    def test_book_form_invalid_isbn(self):
        form = BookForm(data={
            "authors": [self.author.id],
            "title": "poire",
            "publisher": "Newton",
            "year": 1951,
            "isbn": "978-2070360539",
            "backCover": "salut",
            "cover": False,
        })
        self.assertFalse(form.is_valid())
        self.assertIn("isbn", form.errors)


class ViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="knaaaaaaaaa", password="Hung123456@")
        self.author = Author.objects.create(first_name="Maurice", last_name="Leblanc", user=self.user)
        self.book = Book.objects.create(
            user=self.user,
            title="Arsène Lupin",
            publisher="Pierre Lafitte",
            year=1907,
            isbn="978-2253006701",
            backCover="Les aventures du gentleman cambrioleur.",
            cover=False,
        )
        self.book.author.add(self.author)

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Arsène Lupin")

    def test_book_detail_view_and_404(self):
        response = self.client.get(reverse("book", args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        response_404 = self.client.get(reverse("book", args=[9999]))
        self.assertEqual(response_404.status_code, 404)

    def test_new_book_requires_login(self):
        response = self.client.get(reverse("new_book"))
        self.assertEqual(response.status_code, 302)