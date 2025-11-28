from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

# Returns the author's name makes admin and shell outputs more readable.
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

# Displays the book title and year for clarity in admin and shell.
    def __str__(self):
        return f"{self.title} ({self.publication_year})"

