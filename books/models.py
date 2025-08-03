from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Science', 'Science'),
        ('Biographies', 'Biographies'),
        ('Technology', 'Technology'),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='book_images/')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def is_returned(self):
        return self.return_date is not None
