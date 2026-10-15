from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('about', views.about, name='about'),
    path('book/', views.book_list, name='book_list'),
    path('book/new/', views.new_book, name='new_book'),
    path('book/<int:book_id>/', views.book, name='book'),
    path('book/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('book/<int:book_id>/new_review/', views.new_review, name='new_review'),
    path('review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
]