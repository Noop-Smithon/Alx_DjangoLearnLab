<h1>Retrieving a Book Instance<h1>
<br>
<p>from bookshelf.models import Book<p>
<p>Book.objects.filter(title="1984", author="George Orwell")<p>
<br>
'''Terminal returned
<QuerySet [<Book:  Title: 1984, Author: George Orwell, Publication Date: 1949>]>'''
