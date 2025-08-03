from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:book_id>/', views.return_book, name='return_book'),
    path('profile/', views.user_profile, name='user_profile'),

    # Authentication
    path('accounts/', include('django.contrib.auth.urls')),  # login, logout, password reset, etc.
    path('register/', views.register, name='register'),      # registration page
]
