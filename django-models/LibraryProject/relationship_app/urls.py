from django.urls import path
from .views import list_books, LibraryDetailView
from .views import book_list_view, LibraryDetailView, register_view, login_view, logout_view
    

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('books/', views.book_list_view, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('books/', book_list_view, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]