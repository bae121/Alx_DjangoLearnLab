# Advanced API Project

## Overview
This project demonstrates a Django REST Framework API with custom serializers, nested relationships, validation, and secured CRUD endpoints for managing Authors and Books.

---

## Views Configuration

### BookListView
- **Endpoint:** `/api/books/`
- **Purpose:** Retrieve all books.
- **Permissions:** Public (AllowAny).
- **Customizations:** Supports search (`?search=1984`) and ordering (`?ordering=publication_year`).

### BookDetailView
- **Endpoint:** `/api/books/<id>/`
- **Purpose:** Retrieve a single book by ID.
- **Permissions:** Public (AllowAny).

### BookCreateView
- **Endpoint:** `/api/books/create/`
- **Purpose:** Create a new book.
- **Permissions:** Authenticated users only.
- **Customizations:** 
  - Overridden `create()` method to enforce validation.
  - Returns a custom success message with book data.

### BookUpdateView
- **Endpoint:** `/api/books/<id>/update/`
- **Purpose:** Update an existing book.
- **Permissions:** Authenticated users only.
- **Customizations:** 
  - Overridden `update()` method to allow partial updates.
  - Returns a custom success message with updated book data.

### BookDeleteView
- **Endpoint:** `/api/books/<id>/delete/`
- **Purpose:** Delete a book.
- **Permissions:** Authenticated users only.

---

## Custom Settings and Hooks
- **Validation:** `BookSerializer` enforces that `publication_year` cannot be in the future.
- **Permissions:** 
  - Read-only endpoints (`ListView`, `DetailView`) are open to all.
  - Write endpoints (`CreateView`, `UpdateView`, `DeleteView`) require authentication.
- **Filters:** `BookListView` supports search and ordering via DRF’s `SearchFilter` and `OrderingFilter`.
- **Custom Responses:** `CreateView` and `UpdateView` override default methods to return structured JSON messages.

---

## Testing
Usage of Postman to test endpoints:
- `GET /api/books/` → List all books
- `GET /api/books/1/` → Retrieve book by ID
- `POST /api/books/create/` → Create book (requires authentication)
- `PUT /api/books/1/update/` → Update book (requires authentication)
- `DELETE /api/books/1/delete/` → Delete book (requires authentication)

