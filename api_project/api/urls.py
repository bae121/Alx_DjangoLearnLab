from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path ('books/', BookListView.as_view(), name='book-list_create')
]