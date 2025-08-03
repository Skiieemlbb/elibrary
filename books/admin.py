from django.contrib import admin
from django.utils.html import format_html
from .models import Book, BorrowRecord

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_available', 'book_image')
    list_filter = ('category', 'is_available')
    search_fields = ('title', 'author')
    readonly_fields = ['book_image']

    fieldsets = (
        ('Book Details', {
            'fields': ('title', 'author', 'category', 'description')
        }),
        ('Availability & Cover', {
            'fields': ('is_available', 'image', 'book_image')
        }),
    )

    def book_image(self, obj):
        if obj.image:
           return format_html(
    '<img src="{}" style="width: 200px; height: 300px; object-fit: cover; border: 1px solid #ccc;" />',
    obj.image.url
)

        return "No image uploaded"
    book_image.short_description = 'Preview'

admin.site.register(Book, BookAdmin)



class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('user__username', 'book__title')

admin.site.register(BorrowRecord, BorrowRecordAdmin)
