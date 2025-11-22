from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

"""
    BookViewSet below provides full CRUD operations (list, create, retrieve, update, delete).
    Authentication & Permissions:
    - TokenAuthentication ensures that only users with a valid token can access.
    - By default, IsAuthenticated is applied (set in settings.py).
    - You can override permission_classes here if needed.
    Example:
        permission_classes = [IsAdminUser]  # Only admin users can manage books
"""
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
