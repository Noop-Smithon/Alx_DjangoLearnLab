from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(authorName):
    author = Author.objects.get(name = authorName)
    return Book.objects.filter(author = author)

# List all books in a library
def get_books_in_library(libraryName):
    library = Library.objects.get(name = libraryName)
    return library.books.all()

# Retrieve the librarian for a library
def get_librarian_for_library(libraryName):
    library = Librarian.objects.get(library=libraryName)
    return library.librarian