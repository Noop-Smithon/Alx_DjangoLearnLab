<h1>Creating a Book Instance<h1>
<br>
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
<br>
'''Terminal Output
<Book:  Title: 1984, Author: George Orwell, Publication Date: 1949>
'''
