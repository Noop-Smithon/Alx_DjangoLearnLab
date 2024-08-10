<h1>Updating a Book Instance<h1>
<br>
<p>from bookshelf.models import Book<p>
<p>new_book.title = 'Nineteen Eighty-Four'<p>
<p>new_book.save()<p>
<p>Book.objects.all()<p>
<br>
'''Terminal returned
<QuerySet [<Book:  Title: The gods Cry Too, Author: John Doe, Publication Date: 2001>, <Book:  Title: Nineteen Eighty-Four, Author: George Orwell, Publication Date: 1949>]>'''
