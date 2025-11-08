from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

def book_list_view(request):
    books = Book.objects.select_related('author').all()
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output, content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context