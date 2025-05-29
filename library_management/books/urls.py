from django.urls import path
from .views import list_books, loan_book

urlpatterns = [
    path('', list_books, name='books'),
    path('api/loan/<int:book_id>/', loan_book, name='loan_book_api'),  # ✅ Matches JS fetch URL
]
