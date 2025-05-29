from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Book, Loan
import json

def list_books(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books': books})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def loan_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if not book.availability:
        return JsonResponse({'message': 'Book is already loaned.'}, status=400)

    # Check if already loaned by user
    if Loan.objects.filter(user=request.user, book=book).exists():
        return JsonResponse({'message': 'You have already loaned this book.'}, status=400)

    Loan.objects.create(user=request.user, book=book)
    book.availability = False
    book.save()

    return JsonResponse({'message': 'Book loaned successfully.'})
