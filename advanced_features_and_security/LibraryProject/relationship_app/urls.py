from django.urls import path
from .views import list_books, LibraryDetailView
from .views import book_list_view, LibraryDetailView, login_view, logout_view, register, add_book, edit_book, delete_book
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', book_list_view, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
