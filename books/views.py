from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Book, BorrowRecord

from datetime import datetime


def index(request):
    return render(request, 'index.html', {'year': datetime.now().year})



def book_list(request):
    """Displays all books"""
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

# ------------------ Borrow/Return Functionality ------------------

@login_required
def borrow_book(request, book_id):
    """Allows a user to borrow a book if it's available"""
    book = get_object_or_404(Book, id=book_id)

    if book.is_available:
        BorrowRecord.objects.create(user=request.user, book=book)
        book.is_available = False
        book.save()

    return redirect('book_list')


@login_required
def return_book(request, book_id):
    """Handles returning of a borrowed book"""
    book = get_object_or_404(Book, id=book_id)

    # Get the user's active borrow record for the book
    record = BorrowRecord.objects.filter(
        book=book, user=request.user, return_date__isnull=True
    ).first()

    if record:
        record.return_date = timezone.now()
        record.save()

        book.is_available = True
        book.save()

    return redirect('user_profile')


# ------------------ User Profile ------------------

@login_required
def user_profile(request):
    """Displays the current user's borrow history"""
    records = BorrowRecord.objects.filter(user=request.user)
    return render(request, 'profile.html', {'records': records})


# ------------------ User Registration ------------------

def register(request):
    """Handles user registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect('home')  # Use correct home page name
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
