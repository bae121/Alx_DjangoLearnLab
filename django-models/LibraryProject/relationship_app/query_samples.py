from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author (Kofi Akpabli)
akpabli = Author.objects.get(name="Kofi Akpabli")
books_by_akpabli = Book.objects.filter(author=akpabli)
print("Books by Kofi Akpabli:", [book.title for book in books_by_akpabli])

# List all books in a library
library_name = "Central Library"
central_library = Library.objects.get(name="Central Library")
books_in_library = central_library.books.all()
print("Books in Central Library:", [book.title for book in books_in_library])

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=central_library)
print("Librarian of Central Library:", librarian.name)
