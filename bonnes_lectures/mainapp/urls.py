from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('about', views.about, name='about'),
    path('book', views.book_list, name='book_list'),
    path('book/new', views.new_book, name='new_book'),
    path('book/<int:book_id>', views.book, name='book'),
]