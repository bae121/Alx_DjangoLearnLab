from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # The author
        self.author = Author.objects.create(name="Kofi Akpabli")

        # Books by Kofi Akpabli
        self.book1 = Book.objects.create(
            title="Harmattan: A Cultural Profile of Northern Ghana",
            publication_year=2010,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Romancing Ghanaland: The Beauty of Ten Regions",
            publication_year=2009,
            author=self.author
        )

        # Endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book1.id])
        self.delete_url = reverse("book-delete", args=[self.book1.id])

    # LIST
    def test_list_books_public_access(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # RETRIEVE
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harmattan: A Cultural Profile of Northern Ghana")

    # CREATE
    def test_create_book_requires_authentication(self):
        data = {"title": "Tickling the Ghanaian", "publication_year": 2010, "author": self.author.id}
        # Unauthenticated request
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated request
        self.client.login(username="testuser", password="password123")
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["book"]["title"], "Tickling the Ghanaian")

    # UPDATE
    def test_update_book_requires_authentication(self):
        data = {"title": "Harmattan (Updated Edition)", "publication_year": 2010, "author": self.author.id}
        # Unauthenticated request
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated request
        self.client.login(username="testuser", password="password123")
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["book"]["title"], "Harmattan (Updated Edition)")

    # DELETE
    def test_delete_book_requires_authentication(self):
        # Unauthenticated request
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated request
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # FILTERING
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {"title": "Harmattan: A Cultural Profile of Northern Ghana"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # SEARCH
    def test_search_books_by_author_name(self):
        response = self.client.get(self.list_url, {"search": "Akpabli"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ORDERING
    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Harmattan: A Cultural Profile of Northern Ghana")
