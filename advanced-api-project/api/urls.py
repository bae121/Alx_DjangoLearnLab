from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView,BookDeleteView

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve a single book by ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update an existing book (requires ID)
    path('books/update/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book (requires ID)
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
]
