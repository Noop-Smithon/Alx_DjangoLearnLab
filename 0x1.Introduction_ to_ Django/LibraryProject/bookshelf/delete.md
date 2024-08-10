<h1>Deleting a Book Instance<h1>
<br>
<p>from bookshelf.models import Book<p>
<p>Book.objects.filter(title="Nineteen Eighty-Four").delete()<p>
<br>
'''Terminal returned
(1, {'bookshelf.Book': 1})'''
Book.objects.all()
'''Terminal returned
<QuerySet [<Book:  Title: The gods Cry Too, Author: John Doe, Publication Date: 2001>]>'''
