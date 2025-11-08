from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author (Kofi Akpabli)
author_name = "Kofi Akpabli"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by Kofi Akpabli:", [book.title for book in author])

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in Central Library:", [book.title for book in books_in_library])

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian of Central Library:", librarian.name)
